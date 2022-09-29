import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
 
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/preciptation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start></br>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query for the date and precipitation for the last year
    dp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    # Dict with date as the key and prcp as the value
    dp_dict =  {date: prcp for date, prcp in precipitation}
    return jsonify(dp_dict)
 

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    stations = session.query(Measurement.station).group_by(Measurement.station).all()
    # Unravel results into a 1D array and convert to a list
    results = list(np.ravel(stations))
    return jsonify(results)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the primary station for all tobs from the last year
    # tobs = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= year_ago).all()
    tobs = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281', Measurement.date >= '2016-08-23').order_by(Measurement.date).all()

    # Unravel results into a 1D array and convert to a list
    results = list(np.ravel(tobs))
    return jsonify(results)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""
    # Select statement
    select = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # calculate TMIN, TAVG, TMAX with start and stop
    summary = session.query(*select).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    # Unravel results into a 1D array and convert to a list
    results = list(np.ravel(summary))
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

