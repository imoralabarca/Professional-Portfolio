# Group_07

A project dedicated to analyzing the energy mix of several countries, in order to contribute to a greener transition by having a more savvy task force.

## Project: Energy Mix 

## Project overview
We are a company participating in a two-day hackathon promoted to study the energy mix of several countries. We aim to contribute to the green transition by having a more savvy taskforce. The first day is dedicated for code heavy tasks and the second day is focused on polishing and finishing the project for presentation. In this project, using Pandas and Seaborn visualization we will explore the GDP and energy data to obtain an overview of country features.  

## Installation
This project requires Python and the following Python libraries installed: 

- [Pandas](https://pandas.pydata.org) 
- [Matplotlib](https://matplotlib.org) 
- [Plotly-express](https://pypi.org/project/plotly-express/) 
- [Seaborn](https://seaborn.pydata.org/installing.html) 
- Requests 
- Os
- [Statsmodels](https://www.statsmodels.org/stable/install.html)  

You can also install the conda environment that already contains all the libraries needed installed. You are able to find it in the files of the main branch named shut_the_piano.yaml

## Code
The class and all the methods are provided in the ShutThePiano.py file and the data is in the [energy.csv](https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv) file (already downloaded with the __init__ method) 

## Data

From the dataset we used the energy.csv as previously mentioned and some energy sources were chosen to evaluate the emissions and consumptions of the countries. Those are:
- Biofuel
- Coal
- Gas
- Hydro
- Nuclear
- Oil
- Solar
- Wind

## Usage
There are 8 methods included in the project: 

1) **get_data** 
    - This method, when called, downloads the energy-data csv file and saves it into a pandas data frame. 

2) **get_countries** 
    - This method, when called, obtains the unique list of the available countries in the data set. 

3) **area_chart** 
    - The method requests to input chosen country names and outputs an area chart of indexed energy consumption per year. This method contains country and normalize as arguments and needs to be called, for example, as area_chart("Portugal", normalize = True ). In this case, the country name needs to have the first letter capitalized and does not accept short forms, whereas normalize takes both True and False arguments (where with True the data will be normalized, and with False the opposite will occur). 

4) **compare_country** 
    - To call the method you need to use compare_country( ) and then it will request to input a certain amount of countries to compare and then the name of the chosen countries. The output will be a line chart with the energy consumption per year per the selected countries and in addition a dashed line chart with the emissions for the same countries.  

5) **compare_gdp** 
    - This method will output the yearly GDP data for the chosen countries. To instantiate the function, you need to call the compare_gdp( ) method. It will then ask for the number of countries you want to compare, and after filling the gap it will display the exact number of countries chosen. The final output will be a line chart with the gdp for each country throughout the years. 

6) **gapminder** 
    - The gapminder method takes the year and world arguments, and can be used like: gapminder(1992, world = False). This method will output a bubble chart with the energy consumption on the y axis and the gdp on the x axis. Moreover, it also shows the population size for each country as the size of the bubble. Saying so, the year argument has a range from 1970 to 2019 (depending on the countries chosen) and the world represent the aggregated values of all countries. In this case if we display world = False we will not have a bubble for the world, meaning that the rest of the countries will have a more amplified view (easier to analyze). 

7) **arima_model**
    - After calling the method arima_model( ), it will ask the user for the country intends to do the forecast and how many years are pretended to do so. After filling the gaps, the output will be two separatly line charts where the top one represents the forecast of the consumptions for the desired country and the bottom one regards the emissions. It is also possible to check in each graphic, in orange the values registered so far and in blue the model forecast.

8) **emissions_vs_consumption**
    - To initiate this analysis the user needs to call the method emissions_vs_consumption( ) with the respective year they want to analyse inside the brackets (i.e.: emissions_vs_consumption(2000)). After this, the method will display a scatter plot of the consumptions (y axis) and emissions (x axis) for all of the countries of the chosen year. Take into account that the size of the bubbles represents the population of the countries.

## Authors and acknowledgment
Branco, Luís : 50409@novasbe.pt

Esteves, Filipa : 48842@novasbe.pt 

Mora, Isabel : 48516@novasbe.pt 

Paleckyte, Ieva : 48327@novasbe.pt 

## License
GNU GENERAL PUBLIC LICENSE

## Project status
Completed
