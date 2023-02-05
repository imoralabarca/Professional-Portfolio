"""
ShutThePiano Class
"""
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
import plotly_express as px


class ShutThePiano:
    """
    Downloads data, reads it as a pandas dataframe and performs...

    Attributes
    -------------------
    url : str
        Url of the data to save
    name : str
        Name to give the file and dataframe

    Methods
    -------------------
    get_data()
        Downloads the data and reads it into a pandas dataframe
    get_countries()
        Obtains the unique list of countries of the dataset
    area_chart()
        Create a area chart showing the amount of each consumption throughout time
    compare_country()
        Create a line chart with the total of consumptions throughout time for the countries chosen
    compare_gdp()
        Create a line chart with the GDP throughout time for the countries chosen
    gapminder()
        Create a scatter plot that display the gdp vs total energy consumption,
        using the population as the size, for the selected year
    """

    def __init__(
        self,
        url: str = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv",
        name: str = "energy.csv",
    ):

        self.url = url
        self.name = name
        self.dataframe = self.get_data()

        self.country = None
        self.year = None
        self.world = None
        self.normalize = None

    def get_data(self):
        """
        Downloads the data from the url and reads it into a dataframe,
        filtering the year to only after 1970.

        Returns
        ----------------
        A pandas dataframe
        """
        dir_name = "downloads"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print("Directory ", dir_name, " Created ")
        else:
            print("Directory ", dir_name, " already exists")

        file_name = self.name
        url = self.url
        complete_path = os.path.join(dir_name, file_name)

        if not os.path.exists(complete_path):
            try:
                request = requests.get(url)
                url_content = request.content
                with open(complete_path, "wb") as energy_file:
                    energy_file.write(url_content)
                    energy_file.close()
                energy_data = pd.read_csv("downloads/energy.csv")
                energy_data = energy_data[energy_data["year"] >= 1970]

                # updating the data part
                energy_data["new_year"] = energy_data["year"].copy()
                energy_data["new_year"] = pd.to_datetime(
                    energy_data["new_year"], utc=False
                )
                energy_data["new_year"] = energy_data["new_year"].dt.date
                energy_data.set_index(energy_data["new_year"], inplace=True, drop=True)

            except KeyError as key_error:
                print("Something went wrong:", key_error)
        else:
            energy_data = pd.read_csv("downloads/energy.csv")
            energy_data = energy_data[energy_data["year"] >= 1970]

            # updating the data part
            energy_data["new_year"] = energy_data["year"].copy()
            energy_data["new_year"] = pd.to_datetime(energy_data["new_year"], utc=False)
            energy_data["new_year"] = energy_data["new_year"].dt.date
            energy_data.set_index(energy_data["new_year"], inplace=True)
        return energy_data

    def get_countries(self):
        """
        Obtains the unique list of the available countries in the data set

        Returns
        ----------------
        A list
        """
        unique_countries = self.dataframe["country"].unique().tolist()
        return unique_countries

    def area_chart(self, country: str, normalize: bool = True):
        """
        Creates a stacked area chart of the consumption values for a given country.
        The user can change the normalize attribute to have the plot with the data
        un-normalized. By default, the data is normalized so that all the consumptions
        sum up to 100%.

        Parameters
        ----------------
        country: str
            Input of the user
        normalize: boolean
            If the value is true the data will be normalized,
            otherwise if the value is False the data won't be normalized.

        Returns
        ----------------
        A stacked area chart
        """
        self.country = country
        self.normalize = normalize

        if country not in self.get_countries():
            raise TypeError("Country not in list")
        if normalize:
            df_area = self.dataframe[self.dataframe["country"] == country][
                [
                    "year",
                    "biofuel_consumption",
                    "coal_consumption",
                    "gas_consumption",
                    "hydro_consumption",
                    "nuclear_consumption",
                    "oil_consumption",
                    "solar_consumption",
                    "wind_consumption",
                ]
            ].copy()

            df_area.set_index("year", inplace=True)
            normalized_df = df_area.div(df_area.sum(axis=1), axis=0).reset_index()
            normalized_df.plot.area(x="year", figsize=(15, 15))
            plt.xlabel("Year", fontsize=15)
            plt.ylabel("Percentage of Consumption", fontsize=15)
            plt.title("Consumption for a Country", fontsize=17)
            ax_plot = plt.gca()
            handles, labels = ax_plot.get_legend_handles_labels()
            labels, handles = zip(
                *sorted(zip(labels, handles), key=lambda t: t[0], reverse=True)
            )
            ax_plot.legend(handles, labels, loc="upper right")
            plt.show()
        else:
            df_area = self.dataframe[self.dataframe["country"] == country][
                [
                    "year",
                    "biofuel_consumption",
                    "coal_consumption",
                    "gas_consumption",
                    "hydro_consumption",
                    "nuclear_consumption",
                    "oil_consumption",
                    "solar_consumption",
                    "wind_consumption",
                ]
            ].copy()

            df_area.plot.area(x="year", figsize=(15, 15))
            plt.xlabel("Year", fontsize=15)
            plt.ylabel("Percentage of Consumption", fontsize=15)
            plt.title("Consumption for a Country", fontsize=17)
            ax_plot = plt.gca()
            handles, labels = ax_plot.get_legend_handles_labels()
            labels, handles = zip(
                *sorted(zip(labels, handles), key=lambda t: t[0], reverse=True)
            )
            ax_plot.legend(handles, labels, loc="upper right")
            plt.show()

    def compare_country(self):
        """
        Create a line chart that plots the total consumption and emission values
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
        check = all(item in all_countries_list for item in country_list)
        if check is False:
            raise TypeError("One or more countries were mispelled.")
        country_comp = self.dataframe[self.dataframe["country"].isin(country_list)][
            [
                "year",
                "country",
                "gdp",
                "population",
                "biofuel_consumption",
                "coal_consumption",
                "gas_consumption",
                "hydro_consumption",
                "nuclear_consumption",
                "oil_consumption",
                "solar_consumption",
                "wind_consumption",
            ]
        ].copy()
        country_comp = self.dataframe[self.dataframe["country"].isin(country_list)][
            [
                "year",
                "country",
                "biofuel_consumption",
                "coal_consumption",
                "gas_consumption",
                "hydro_consumption",
                "nuclear_consumption",
                "oil_consumption",
                "solar_consumption",
                "wind_consumption",
            ]
        ]
        country_comp.fillna(0, inplace=True)
        # Total Consumption
        country_comp["total_consumption"] = country_comp.iloc[:, 2:].sum(axis=1)
        # Emissions
        consumptions = [
            "biofuel_consumption",
            "coal_consumption",
            "gas_consumption",
            "hydro_consumption",
            "nuclear_consumption",
            "oil_consumption",
            "solar_consumption",
            "wind_consumption",
        ]
        emissions_gperkwh = [1450, 1000, 455, 90, 5.5, 1200, 53, 14]
        emissions_tpertwh = [item / 1000 for item in emissions_gperkwh]
        for key, value in zip(consumptions, emissions_tpertwh):
            country_comp["emissions_{}".format(key)] = round(
                country_comp[key].apply(lambda x: x * value), 2
            )
        country_comp["total_emissions"] = round(
            country_comp[
                [
                    "emissions_biofuel_consumption",
                    "emissions_coal_consumption",
                    "emissions_gas_consumption",
                    "emissions_hydro_consumption",
                    "emissions_nuclear_consumption",
                    "emissions_oil_consumption",
                    "emissions_solar_consumption",
                    "emissions_wind_consumption",
                ]
            ].sum(axis=1),
            2,
        )

        # Plot
        fig, ax = plt.subplots(figsize=(12, 8), dpi=600)
        line_1 = sns.lineplot(
            x="year",
            y="total_consumption",
            hue="country",
            data=country_comp.reset_index(),
        )
        ax.set_title("Total Consumptions and emissions", fontweight="bold", fontsize=20)
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Consumptions")
        # Emissions
        ax2 = ax.twinx()
        line_2 = sns.lineplot(
            data=country_comp.reset_index(),
            x="year",
            y="total_emissions",
            hue="country",
            linestyle="--",
        )
        ax2.set_ylabel("Total Emissions")
        # Legend
        ax.legend()

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
        check = all(item in all_countries_list for item in country_list)
        if check is False:
            raise TypeError("One or more countries were mispelled.")

        gdp_comp = self.dataframe[self.dataframe["country"].isin(country_list)][
            ["year", "country", "gdp"]
        ]
        plt.figure(figsize=(12, 10))
        plt.title("GDP values over the years", fontweight="bold", fontsize=20)
        sns.lineplot(x="year", y="gdp", hue="country", data=gdp_comp.reset_index())
        plt.xlabel("Year")
        plt.ylabel("GDP")
        plt.show()

    def gapminder(self, year: int, world: bool = False):
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
        check = year in all_year_list
        if check is False:
            raise TypeError(
                "There is no data for the year selected. Please insert a value between 1970 and 2016."
            )

        try:
            if world:
                gapminder_df = self.dataframe[self.dataframe["year"] == year][
                    [
                        "year",
                        "country",
                        "gdp",
                        "population",
                        "biofuel_consumption",
                        "coal_consumption",
                        "gas_consumption",
                        "hydro_consumption",
                        "nuclear_consumption",
                        "oil_consumption",
                        "solar_consumption",
                        "wind_consumption",
                    ]
                ].copy()
            else:
                gapminder_df = self.dataframe[
                    (self.dataframe["year"] == year)
                    & (self.dataframe["country"] != "World")
                ][
                    [
                        "year",
                        "country",
                        "gdp",
                        "population",
                        "biofuel_consumption",
                        "coal_consumption",
                        "gas_consumption",
                        "hydro_consumption",
                        "nuclear_consumption",
                        "oil_consumption",
                        "solar_consumption",
                        "wind_consumption",
                    ]
                ].copy()

        except TypeError:
            print("The year needs to be integer.")
        finally:
            gapminder_df["total"] = gapminder_df.iloc[:, 4:].sum(axis=1)

            gapminder_df.fillna(0, inplace=True)
            fig = px.scatter(
                gapminder_df.reset_index(),
                x="gdp",
                y="total",
                size="population",
                color="country",
                animation_frame="year",
                animation_group="country",
                hover_name="country",
                log_x=True,
                log_y=True,
                size_max=45,
                width=1200,
                height=1000,
                labels={
                    "gdp": "Total GDP",
                    "total": "Total Consumption (TwH)",
                    "country": "Country",
                },
                title="GDP vs Total Consumption for each Country",
            )
            fig.show()

    def emissions_vs_consumption(self, year: int):
        """
        This method returns a scatter plot displaying the total consumption
        vs the total emissions for every country throughout the years

        Parameters
        ----------------
        year: int
            Period of time for the information

        Returns
        ----------------
        A scatter plot
        """
        self.year = year
        all_year_list = self.dataframe["year"].unique().tolist()
        check = year in all_year_list
        if check is False:
            raise TypeError(
                "There is no data for the year selected. Please insert a value between 1970 and 2019."
            )

        remove_agg = [
            "Africa",
            "Europe",
            "World",
            "CIS",
            "Asia Pacific",
            "Central America",
            "Eastern Africa",
            "Europe (other)",
            "Middle Africa",
            "Middle East",
            "North America",
            "OPEC",
            "Other Asia & Pacific",
            "Other CIS",
            "Other Caribbean",
            "Other Middle East",
            "Other Northern Africa",
            "Other South America",
            "Other Southern Africa",
            "South & Central America",
            "Western Africa",
        ]
        scatter_df = self.dataframe[
            (self.dataframe["country"].isin(remove_agg) == False)
            & (self.dataframe["year"] == year)
        ][
            [
                "year",
                "country",
                "population",
                "biofuel_consumption",
                "coal_consumption",
                "gas_consumption",
                "hydro_consumption",
                "nuclear_consumption",
                "oil_consumption",
                "solar_consumption",
                "wind_consumption",
            ]
        ].copy()
        scatter_df["total_consumption"] = scatter_df.iloc[:, 3:].sum(axis=1)
        # Emissions
        consumptions = [
            "biofuel_consumption",
            "coal_consumption",
            "gas_consumption",
            "hydro_consumption",
            "nuclear_consumption",
            "oil_consumption",
            "solar_consumption",
            "wind_consumption",
        ]
        emissions_gperkwh = [1450, 1000, 455, 90, 5.5, 1200, 53, 14]
        emissions_tpertwh = [item / 1000 for item in emissions_gperkwh]
        for key, value in zip(consumptions, emissions_tpertwh):
            scatter_df["emissions_{}".format(key)] = round(
                scatter_df[key].apply(lambda x: x * value), 2
            )
        scatter_df["total_emissions"] = round(
            scatter_df[
                [
                    "emissions_biofuel_consumption",
                    "emissions_coal_consumption",
                    "emissions_gas_consumption",
                    "emissions_hydro_consumption",
                    "emissions_nuclear_consumption",
                    "emissions_oil_consumption",
                    "emissions_solar_consumption",
                    "emissions_wind_consumption",
                ]
            ].sum(axis=1),
            2,
        )
        scatter_df.fillna(0, inplace=True)
        fig = px.scatter(
            scatter_df.reset_index(),
            x="total_emissions",
            y="total_consumption",
            size="population",
            color="country",
            animation_frame="year",
            animation_group="country",
            hover_name="country",
            labels={
                "total_emissions": "Total Emissions (TonCO2p/TwH)",
                "total_consumption": "Total Consumption (TwH)",
                "country": "Country",
            },
            width=1000,
            height=600,
            log_x=True,
            range_x=[1, 200000],
            log_y=True,
            range_y=[1, 200000],
            title="Total Consumption vs Total Emissions for each Country",
        )
        fig.show()

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

        country_comp = self.dataframe[self.dataframe["country"] == country_id][
            [
                "year",
                "country",
                "biofuel_consumption",
                "coal_consumption",
                "gas_consumption",
                "hydro_consumption",
                "nuclear_consumption",
                "oil_consumption",
                "solar_consumption",
                "wind_consumption",
            ]
        ]

        country_comp.fillna(0, inplace=True)
        country_comp["total"] = country_comp.iloc[:, 2:].sum(axis=1)
        country_comp.set_index("year", inplace=True)

        train = country_comp[:-2]

        custom_train_index = pd.DatetimeIndex(train.index.values, freq="infer")

        model = ARIMA(train["total"].values, order=(5, 1, 1), dates=custom_train_index)
        model_fit = model.fit()
        forecast_data = model_fit.predict(
            len(train), len(train) + npts - 1, typ="levels"
        )
        starting_year = train.index[-1] + 1
        ending_year = train.index[-1] + npts + 1
        forecast_index = [x for x in range(starting_year, ending_year)]
        forecast = pd.Series(data=forecast_data, index=forecast_index)

        consumptions = [
            "biofuel_consumption",
            "coal_consumption",
            "gas_consumption",
            "hydro_consumption",
            "nuclear_consumption",
            "oil_consumption",
            "solar_consumption",
            "wind_consumption",
        ]

        emissions_gperkwh = [1450, 1000, 455, 90, 5.5, 1200, 53, 14]
        emissions_tpertwh = [item / 1000 for item in emissions_gperkwh]
        for key, value in zip(consumptions, emissions_tpertwh):
            country_comp["emissions_{}".format(key)] = round(
                country_comp[key].apply(lambda x: x * value), 2
            )
        country_comp["emissions"] = round(
            country_comp[
                [
                    "emissions_biofuel_consumption",
                    "emissions_coal_consumption",
                    "emissions_gas_consumption",
                    "emissions_hydro_consumption",
                    "emissions_nuclear_consumption",
                    "emissions_oil_consumption",
                    "emissions_solar_consumption",
                    "emissions_wind_consumption",
                ]
            ].sum(axis=1),
            2,
        )

        train_e = country_comp[:-2]
        custom_train_index_e = pd.DatetimeIndex(train_e.index.values, freq="infer")

        model = ARIMA(
            train_e["emissions"].values, order=(5, 1, 1), dates=custom_train_index_e
        )
        model_fit_e = model.fit()
        forecast_data_e = model_fit_e.predict(
            len(train_e), len(train_e) + npts - 1, typ="levels"
        )
        starting_year = train_e.index[-1] + 1
        ending_year = train_e.index[-1] + npts + 1
        forecast_index = [x for x in range(starting_year, ending_year)]
        forecast_e = pd.Series(data=forecast_data_e, index=forecast_index)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        ax1.plot(forecast, "r--", label="Consumption Forecast")
        ax1.plot(train["total"], "g", label="Consumption Historic Trend")
        ax1.legend(loc="lower center", shadow=True, fontsize="large")
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Total Consumption (TwH)")
        ax1.set_title(f"{country_id} Total Consumption")

        ax2.plot(forecast_e, "r--", label="Emissions Forecast")
        ax2.plot(train_e["emissions"], "g", label="Emissions Historic Trend")
        ax2.legend(loc="lower center", shadow=True, fontsize="large")
        ax2.set_xlabel("Year")
        ax2.set_ylabel("Total Emissions (TonCO2p/TwH)")
        plt.title(f"{country_id} Total Emissions")
        plt.show()
