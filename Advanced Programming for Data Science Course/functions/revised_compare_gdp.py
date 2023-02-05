def compare_gdp(self):
    """
    Create a line chart that compares the GDP throughout time for the country/countries given.

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

    gdp_comp = self.dataframe[self.dataframe["country"].isin(countries_list)][["year",
                                                                               "country",
                                                                               "gdp"]]
    plt.figure(figsize=(12,10))
    sns.lineplot(x="year", y="gdp",
         hue="country",
         data=gdp_comp)