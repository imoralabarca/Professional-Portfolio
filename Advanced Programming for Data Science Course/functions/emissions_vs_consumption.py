def emissions_vs_consumption(self):
    """
    This method returns a scatter plot displaying the total consumption
    vs the total emissions for every country throughout the years

    Returns
    ----------------
    A scatter plot
    """
    scatter_df = self.dataframe[['year', 'country', 'population', 
                                 'biofuel_consumption','coal_consumption', 
                                 'gas_consumption', 'hydro_consumption', 
                                 'nuclear_consumption', 'oil_consumption', 
                                 'solar_consumption', 'wind_consumption' ]].copy()
    scatter_df["total_consumption"] = scatter_df.iloc[:, 3:].sum(axis=1)
    # Emissions
    consumptions = ['biofuel_consumption','coal_consumption', 'gas_consumption',
            'hydro_consumption', 'nuclear_consumption', 'oil_consumption',
            'solar_consumption', 'wind_consumption']
    emissions_gperkwh = [1450, 1000, 455, 90, 5.5, 1200, 53, 14]
    emissions_tpertwh = [item/1000 for item in emissions_gperkwh]
    for key, value in zip(consumptions, emissions_tpertwh):
        scatter_df["emissions_{}".format(key)] = round(scatter_df[key].apply(lambda x : x * value), 2)
    scatter_df["total_emissions"] = round(scatter_df[['emissions_biofuel_consumption',
                                                        'emissions_coal_consumption',
                                                        'emissions_gas_consumption',
                                                        'emissions_hydro_consumption',
                                                        'emissions_nuclear_consumption',
                                                        'emissions_oil_consumption',
                                                        'emissions_solar_consumption',
                                                        'emissions_wind_consumption']].sum(axis=1), 2)
    scatter_df.fillna(0, inplace=True)
    fig = px.scatter(scatter_df, x="total_emissions", y="total_consumption", size="population", color="country",
                     animation_frame="year", animation_group="country", hover_name="country", log_x = True,
                     log_y = True, labels={"total_emissions": "Total Emissions (TonCO2p/TwH)",
                                           "total_consumption": "Total Consumption (TwH)",
                                           "country": "Country"}, width=1000, height=600,
                     title="Total Consumption vs Total Emissions for each Country")
    fig.show()