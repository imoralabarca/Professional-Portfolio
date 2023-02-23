# Data Visualization Final Project


The questions that we wanted to explore through our dashboards were: 
- **1.	Dashboard “Terrorism Overview”: Overall, what have been the countries most attacked in both number of attacks and casualties, by year.**
- a.	In the countries/regions of interest of the group (Europe and Venezuela), we wanted to know the development of terrorist attacks across years.
- **2.	Dashboard “Weapons and Target”: How do weapon type changes depending on target type?**
- a.	We added the possibility for the user to select a region or decade of interest, and to display the casualties by weapon type to avoid misleading information (For example, fake weapons are mostly used in airports, but for obvious reasons the casualties are 0)
- **3.	Dashboard “Countries Freedom”: Are free countries less vulnerable than not free countries ?**
- a.	Because instability in the countries depend a lot on the region, we wanted to make this dashboard as interactive as possible so that the user can inspect specifically one country at a time and with the visualizations on the bottom compare across periods where that country was not free or partially free. For example, we found that Venezuela had more terrorist attacks during the period that it was free, and that the main target was the government. On the contrary, while it’s been not free, the main target has been the police. 
- **4.	Dashboard “Terrorist Groups”: Is there a relationship between terrorists’ groups years of activity and total amount of attacks?**
- a.	Depends on each terrorist group. We were able to find out that older groups are not as violent in the same rate as the newer ones. If the newer ones keep up the pace, by the time they reach the same years of activity as the older ones, they will have more attacks accumulated, on average
- **5.	Dashboard “Terrorism Density”: What are the most dangerous countries if we look at terrorist attacks per 1 million citizens?** 
- a.	We were able to see that countries such as El Salvador have the highest rate of terrorist attacks per citizens. This dashboard allows users to select a specific country and find out the most dangerous cities based on that metric

Other remarks:
- 1.	Data cleaning (DataViz_DC.ipynb)
- This notebook displays the code used to clean the dataset. Most important issues: only selected fields with less than 2% of null values (confirming this information with TableauPrep). Rows with null values in Days were filled by the mean. Categorical variables with -9 or -99 were replaced with “Unknown”. A new column was created, “Casualties”, to add Wounded and Killed.
- 2.	External data (Adding_data.ipynb)
- This notebook was used to add external data, such as GDP, population and the Freedom House Index of each country, by year. We added an identifier, “Country_year”, as key to add the external data. 
- 3.	Tableau
-- a.	Unknown countries and cities
---i.	We changed the name of unknown, currently nonexistent countries, to those that are currently located were these countries were.
---ii.	There were around 30k cities that still remained unknown, so we decided to use instead the Latitude and Longitude given by the dataset, which mostly corrected the issue, leaving only around 2k null values.
-- b.	Several calculated fields were created to help us achieve the desired results, such as:
---i.	Casualties by attack, % of count(eventid), Terrorism density, Years Active, and other LOD expressions.


