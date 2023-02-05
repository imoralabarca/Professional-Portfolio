def area_chart(self, country : str , normalize : bool = True):
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
                df_area = self.dataframe[self.dataframe["country"] == country][["year", 'biofuel_consumption',
                 'coal_consumption',
                 'fossil_fuel_consumption',
                 'gas_consumption',
                 'hydro_consumption',
                 'low_carbon_consumption',
                 'nuclear_consumption',
                 'oil_consumption',
                 'other_renewable_consumption',
                 'primary_energy_consumption',
                 'renewables_consumption',
                 'solar_consumption',
                 'wind_consumption']]
                                
                df_area.set_index("year", inplace = True)
                normalized_df = df_area.div(df_area.sum(axis=1), axis=0).reset_index()
                normalized_df.plot.area(x="year", figsize=(15,15))
                plt.xlabel('Year', fontsize=15)
                plt.ylabel('Percentage of Consumption', fontsize=15)
                plt.title('Consumption for a Country',fontsize=17)
                ax_plot = plt.gca()
                handles, labels = ax_plot.get_legend_handles_labels()
                labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0], reverse=True))
                ax_plot.legend(handles, labels, loc="upper right")
                plt.show()

        else:
            df_area = self.dataframe[self.dataframe["country"] == country][["year", 'biofuel_consumption',
             'coal_consumption',
             'fossil_fuel_consumption',
             'gas_consumption',
             'hydro_consumption',
             'low_carbon_consumption',
             'nuclear_consumption',
             'oil_consumption',
             'other_renewable_consumption',
             'primary_energy_consumption',
             'renewables_consumption',
             'solar_consumption',
             'wind_consumption']]

            df_area.plot.area(x="year", figsize=(15,15))
            plt.xlabel('Year', fontsize=15)
            plt.ylabel('Percentage of Consumption', fontsize=15)
            plt.title('Consumption for a Country',fontsize=17)
            ax_plot = plt.gca()
            handles, labels = ax_plot.get_legend_handles_labels()
            labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0], reverse=True))
            ax_plot.legend(handles, labels, loc="upper right")
            plt.show()