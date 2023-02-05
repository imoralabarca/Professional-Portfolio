def get_countries(self):
    """
    Obtains the unique list of the available countries in the data set
    
    Returns
    ----------------
    A list
    """
    unique_countries = self.dataframe['country'].unique().tolist()
    return unique_countries


def compare_country(self):
    """
    Create a line chart that compares the total of consumptions throughout time,
    for the country/countries given.
    Returns
    ----------------
    A line chart
    """
    nr_countries = int(input("Please insert the number of countries to compare: "))
    country_list = []
    for i in range(nr_countries):

        country = str(input("Insert the name of the Country: "))
        country_list.append(country)

    all_countries_list = self.dataframe["country"].unique().tolist()
    check =  all(item in all_countries_list for item in country_list)
    if check is False:
        raise TypeError("One or more countries were mispelled.")

    country_comp = self.dataframe[self.dataframe["country"].isin(inputt)][["year", "country", 'biofuel_consumption',
                                                                     'coal_consumption', 'fossil_fuel_consumption',
                                                                     'gas_consumption', 'hydro_consumption',
                                                                     'low_carbon_consumption', 'nuclear_consumption',
                                                                     'oil_consumption', 'other_renewable_consumption',
                                                                     'primary_energy_consumption', 'renewables_consumption',
                                                                     'solar_consumption', 'wind_consumption']]

    country_comp.fillna(0, inplace=True)
    country_comp["total"] = country_comp.iloc[:, 2:].sum(axis=1)
    plt.figure(figsize=(12,10))
    sns.lineplot(x="year", y="total", hue="country", data=country_comp)
