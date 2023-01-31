# SQLAlchemy Climate Analysis 

### Part 1: Climate Analysis and Exploration

In this section, you’ll use Python and SQLAlchemy to perform basic climate analysis and data exploration of your climate database. Complete the following tasks by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use SQLAlchemy’s `create_engine` to connect to your SQLite database.

![carbon (11)](https://user-images.githubusercontent.com/107604123/215658367-0968607b-f81e-4ad8-bc61-c949bb3d4078.png)

* Use SQLAlchemy’s `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

![carbon (12)](https://user-images.githubusercontent.com/107604123/215658510-fedb835c-2515-420c-9f94-c11b294d4e4e.png)

* Link Python to the database by creating a SQLAlchemy session.

![carbon (13)](https://user-images.githubusercontent.com/107604123/215658597-cf568173-bd1a-46c0-8518-0e04cd660d53.png)

#### Precipitation Analysis

To perform an analysis of precipitation in the area, do the following:

* Find the most recent date in the dataset.

![carbon (14)](https://user-images.githubusercontent.com/107604123/215658674-673272e9-3d80-45fc-b0cd-b6db261b193e.png)

* Using this date, retrieve the previous 12 months of precipitation data by querying the 12 previous months of data. Select only the `date` and `prcp` values.

![carbon (15)](https://user-images.githubusercontent.com/107604123/215658910-384dea55-2348-487a-9d9f-ca2056ae4b77.png)

* Load the query results into a Pandas DataFrame, and set the index to the date column. Sort the DataFrame values by `date`.

![carbon (16)](https://user-images.githubusercontent.com/107604123/215658963-ffeb7e95-3818-4976-ad2d-eea1859e1eca.png)

* Plot the results by using the DataFrame `plot` method.

![carbon (17)](https://user-images.githubusercontent.com/107604123/215659018-b3ba07ce-05f5-45b3-b7c7-4534455eaeb3.png)

* Use Pandas to print the summary statistics for the precipitation data.

/Users/brittanieocampo/Desktop/DATA/SQL-Alchemy-Challenge/Images/precip.png

#### Station Analysis

To perform an analysis of stations in the area, do the following:

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (the stations with the most rows).

    * List the stations and observation counts in descending order.

    * Which station id has the highest number of observations?

    * Using the most active station id, calculate the lowest, highest, and average temperatures.

    * **Hint:** You will need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations.

    * Query the previous 12 months of temperature observation data for this station.

    * Plot the results as a histogram with `bins=12`, as shown in the following image:

    ![station-histogram](Images/station-histogram.png)

* Close out your session.

- - -

### Part 2: Design Your Climate App

Now that you have completed your initial analysis, you’ll design a Flask API based on the queries that you have just developed.

Use Flask to create your routes, as follows:

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).

## Hints

* You will need to join the station and measurement tables for some of the queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.

### Bonus: Other Recommended Analyses

The following are optional challenge queries that we recommend you attempt, but they are not required for this assignment.

* Use the provided [temp_analysis_bonus_1_starter.ipynb](temp_analysis_bonus_1_starter.ipynb) and [temp_analysis_bonus_2_starter.ipynb](temp_analysis_bonus_2_starter.ipynb) starter notebooks for their respective bonus challenge.

#### Temperature Analysis 1

Conduct an analysis to answer the following question: Hawaii is reputed to enjoy mild weather all year round. Is there a meaningful difference between the temperatures in, for example, June and December?

* Use Pandas to perform the following steps:

    * Convert the date column format from `string` to `datetime`.

    * Set the date column as the DataFrame index.

    * Drop the date column.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for the temperature in December.

* Use the t-test to determine whether the difference in means, if any, is statistically significant. Will you use a paired t-test or an unpaired t-test? Why?

#### Temperature Analysis 2

You want to take a trip from August 1 to August 7 of this year, but you are worried that the weather will be less than ideal. Using historical data in the dataset, find out what the temperature has previously been for this timeframe.

**Note:** The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

Complete the following steps:

* Use the `calc_temps` function to calculate the minimum, average, and maximum temperatures for your trip using the matching dates from a previous year (for example, use "2017-08-01").

* Plot the minimum, average, and maximum temperature from your previous query as a bar chart, as captured in the following steps and image:

    * Use "Trip Avg Temp" as the title.

    * Use the average temperature as the bar height (_y_ value).

    * Use the peak-to-peak (TMAX-TMIN) value as the _y_ error bar (YERR).

    ![temperature](Images/temperature.png)

#### Daily Rainfall Average

Now that you have an idea of the temperature, let’s find out what the rainfall has been. You don't want to visit if it rains the whole time! Complete the following steps:

* Calculate the rainfall per weather station using the previous year's matching dates.

    * Sort this in descending order by precipitation amount, and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals

Calculate the daily normals for the duration of your trip. Normals are the averages for the minimum, average, and maximum temperatures.

You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Make sure to use all historic TOBS that match that date string.

Complete the following steps:

* Set the start and end date of the trip.

* Use the date to create a range of dates.

* Strip off the year, and save a list of strings in the format `%m-%d`.

* Use the `daily_normals` function to calculate the normals for each date string, and append the results to a list called `normals`.

* Load the list of daily normals into a Pandas DataFrame, and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals, as shown in the following image:

  ![daily-normals](Images/daily-normals.png)

* Close out your session.

## Rubric

[Unit 10 Homework Rubric](https://docs.google.com/document/d/1gT29iMF3avSvJruKpcHY4qovP5QitgXePqtjC6XESI0/edit?usp=sharing)

- - -

## References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
