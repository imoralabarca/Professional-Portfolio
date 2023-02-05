def gapminder(self, year : int, world : bool = False):
    """
    Create a scatter plot that display the gdp vs total energy consumption,
    using the population as the size, for the selected year.
    
    Parameters
    ----------------
    world: bool
        Data point that contains the sum of all the other points
    year: int
        Period of time for the information
    
    Returns
    ----------------
    A scatter plot
    """
    self.world = world
    self.year = year

    all_year_list = self.dataframe["year"].unique().tolist()
    check =  year in all_year_list
    if check is False:
        raise TypeError("There is no data for the year selected. Please insert a value between 1970 and 2016.")

    try:
        if world:
            gapminder_df = self.dataframe[self.dataframe["year"] == year][["year", "country", "gdp",
                                                                     "population", 'biofuel_consumption',
                                                                     'coal_consumption', 'fossil_fuel_consumption',
                                                                     'gas_consumption', 'hydro_consumption',
                                                                     'low_carbon_consumption', 'nuclear_consumption',
                                                                     'oil_consumption', 'other_renewable_consumption',
                                                                     'primary_energy_consumption', 'renewables_consumption',
                                                                     'solar_consumption', 'wind_consumption']]
        else:
            gapminder_df = self.dataframe[(self.dataframe["year"] == year) &
                             (self.dataframe["country"] != "World")][["year", "country", "gdp",
                                                                     "population", 'biofuel_consumption',
                                                                     'coal_consumption', 'fossil_fuel_consumption',
                                                                     'gas_consumption', 'hydro_consumption',
                                                                     'low_carbon_consumption', 'nuclear_consumption',
                                                                     'oil_consumption', 'other_renewable_consumption',
                                                                     'primary_energy_consumption', 'renewables_consumption',
                                                                     'solar_consumption', 'wind_consumption']]
    except TypeError:
        print("The year needs to be integer.")
    finally:
        gapminder_df["total"] = gapminder_df.iloc[:, 4:].sum(axis=1)

        gapminder_df.fillna(0, inplace=True)
        fig = px.scatter(gapminder_df, x="gdp", y="total", size="population", color="country",
                         animation_frame="year", animation_group="country", hover_name="country", log_x = True,
                         log_y = True, size_max=45, width=1200, height=1000)
        fig.show()