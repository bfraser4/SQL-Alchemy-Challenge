# SQLAlchemy Climate Analysis & Flask API Application Build

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
![Screen Shot 2023-01-30 at 7 58 15 PM](https://user-images.githubusercontent.com/107604123/215659483-bf8bde4b-9884-424e-81ab-dfef41de0988.png)

* Use Pandas to print the summary statistics for the precipitation data.

![carbon (18)](https://user-images.githubusercontent.com/107604123/215659415-2b034473-1e30-4125-b2ca-5ee3b967bb93.png)


#### Station Analysis

To perform an analysis of stations in the area, do the following:

* Design a query to calculate the total number of stations in the dataset.

![carbon (19)](https://user-images.githubusercontent.com/107604123/215659567-83ea947c-1dbd-4d06-9e31-61cf94e91283.png)

* Design a query to find the most active stations (the stations with the most rows).

    * List the stations and observation counts in descending order.
   
      ![carbon (20)](https://user-images.githubusercontent.com/107604123/215659753-91ce5e87-b5c9-4bf8-b8b1-6277e2bd07e7.png)

    * Which station id has the highest number of observations?
   
      ![carbon (21)](https://user-images.githubusercontent.com/107604123/215659846-c8d4ceda-7f5e-4e44-a8cf-66473ad84c54.png)

    * Using the most active station id, calculate the lowest, highest, and average temperatures.
 
      ![carbon (22)](https://user-images.githubusercontent.com/107604123/215660444-a037a04d-8603-4ea8-8b92-25b2a7426272.png)


* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations. Query the previous 12 months of temperature observation data for this station.
   
      ![carbon (23)](https://user-images.githubusercontent.com/107604123/215660305-dce01f5d-fcc1-4f81-8532-40c8e1af9f5a.png)

    * Plot the results as a histogram with `bins=12`.
   
      ![carbon (24)](https://user-images.githubusercontent.com/107604123/215660408-ea332099-49ac-499c-bcea-956ede84788a.png)
      ![Screen Shot 2023-01-30 at 8 07 00 PM](https://user-images.githubusercontent.com/107604123/215660491-aaefedf2-d17d-4e1e-9b45-bf8a1f501bdf.png)

* Close out your session.

![carbon (25)](https://user-images.githubusercontent.com/107604123/215660546-20193ac1-0680-4326-8707-e684cb09c068.png)

- - -

### Part 2: Design Your Climate App

Now that you have completed your initial analysis, you’ll design a Flask API based on the queries that you have just developed.

Creating the Database connection 

![carbon (26)](https://user-images.githubusercontent.com/107604123/215660890-6357c6ea-7d4d-4bc1-a26b-040ce1a06131.png)

Use Flask to create your routes, as follows:

* `/`

    * Homepage.

    * List all available routes.
    ![carbon (27)](https://user-images.githubusercontent.com/107604123/215661035-c8661d81-1f06-4b37-9fc4-ce8a83ab1d39.png)

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.
    ![carbon (28)](https://user-images.githubusercontent.com/107604123/215661155-5f4c2246-c424-4028-be2b-f116a8385858.png)

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.
    ![carbon (29)](https://user-images.githubusercontent.com/107604123/215661227-7df49a1b-448d-4a06-a7be-7a674c719c65.png)

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.
    ![carbon (30)](https://user-images.githubusercontent.com/107604123/215661302-33b8daa3-b04f-4cb4-9b48-fe625195b505.png)


* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date.
    ![carbon (31)](https://user-images.githubusercontent.com/107604123/215661385-6212d35f-0343-49cb-a8b8-18607e1b6797.png)


## Rubric

[Unit 10 Homework Rubric](https://docs.google.com/document/d/1gT29iMF3avSvJruKpcHY4qovP5QitgXePqtjC6XESI0/edit?usp=sharing)

- - -

## References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
