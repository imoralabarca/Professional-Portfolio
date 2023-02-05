def arima_model(self):
    """
    This method returns two line charts where the one on the left represents
    the total consumptions and its forecast, and the one on the right shows
    the total emissions and once again its future predictions
   
    Returns
    ----------------
    Two line charts
    """
    country_id = input("Which country would you like to predict?")
    npts = int(input("How many period would you like to predict?"))

    country_comp = self.dataframe[self.dataframe["country"] == country_id][["year", "country", 'biofuel_consumption',
                                                     'coal_consumption', 'gas_consumption', 'hydro_consumption', 
                                                    'nuclear_consumption','oil_consumption',
                                                'solar_consumption', 'wind_consumption']]

    country_comp.fillna(0, inplace=True)
    country_comp["total"] = country_comp.iloc[:, 2:].sum(axis=1)
    country_comp.set_index('year', inplace=True)

    train = country_comp[:-2]

    custom_train_index = pd.DatetimeIndex(train.index.values,
                           freq="infer")

    model = ARIMA(train['total'].values, order=(5,1,1), dates=custom_train_index)
    model_fit = model.fit()
    forecast_data = model_fit.predict(len(train), len(train)+npts-1, typ="levels")
    starting_year = train.index[-1] + 1
    ending_year = train.index[-1] + npts + 1
    forecast_index = [x for x in range(starting_year,ending_year)]
    forecast = pd.Series(data = forecast_data, index = forecast_index)


    consumptions = ['biofuel_consumption','coal_consumption', 'gas_consumption',
            'hydro_consumption', 'nuclear_consumption', 'oil_consumption',
            'solar_consumption', 'wind_consumption']

    emissions_gperkwh = [1450, 1000, 455, 90, 5.5, 1200, 53, 14]
    emissions_tpertwh = [item/1000 for item in emissions_gperkwh]
    for key, value in zip(consumptions, emissions_tpertwh):
        country_comp["emissions_{}".format(key)] = round(country_comp[key].apply(lambda x : x * value), 2)
    country_comp["emissions"] = round(country_comp[['emissions_biofuel_consumption',
                                                        'emissions_coal_consumption',
                                                        'emissions_gas_consumption',
                                                        'emissions_hydro_consumption',
                                                        'emissions_nuclear_consumption',
                                                        'emissions_oil_consumption',
                                                        'emissions_solar_consumption',
                                                        'emissions_wind_consumption']].sum(axis=1), 2)

    train_e = country_comp[:-2]
    custom_train_index_e = pd.DatetimeIndex(train_e.index.values,
                           freq="infer")

    model = ARIMA(train_e['emissions'].values, order=(5,1,1), dates=custom_train_index_e)
    model_fit_e = model.fit()
    forecast_data_e = model_fit_e.predict(len(train_e), len(train_e)+npts-1, typ="levels")
    starting_year = train_e.index[-1] + 1
    ending_year = train_e.index[-1] + npts + 1
    forecast_index = [x for x in range(starting_year,ending_year)]
    forecast_e = pd.Series(data = forecast_data_e, index = forecast_index)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

    ax1.plot(forecast, 'r--', label='Consumption Forecast')
    ax1.plot(train['total'], 'g', label='Consumption Historic Trend')
    ax1.legend(loc='lower center', shadow=True, fontsize='large')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Total Consumption (TwH)")
    ax1.set_title(f"{country_id} Total Consumption")

    ax2.plot(forecast_e, 'r--', label='Emissions Forecast')
    ax2.plot(train_e['emissions'], 'g', label='Emissions Historic Trend')
    ax2.legend(loc='lower center', shadow=True, fontsize='large')
    ax2.set_xlabel("Year")
    ax2.set_ylabel ("Total Emissions (TonCO2p/TwH)")
    plt.title(f"{country_id} Total Emissions")
    plt.show()