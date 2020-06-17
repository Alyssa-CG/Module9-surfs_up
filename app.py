# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#set up db engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the db into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# create variables for the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from Python to the db
session = Session(engine)

# create a Flask application (called "app")
app = Flask(__name__)

# Define the welcome route (which will be our root, or effectively homepage.)
# NOTE: all routes should be after the app = Flask(__name__) or may not run properly.
@app.route("/")

def welcome():
	return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Run in terminal as:
# export FLASK_APP=app.py
# then:
# flask run
# the paste url into browser to see output.
# NOTE: Every time you create a new route, your code should be aligned to the left in order to avoid errors.

# next route, so precipitation analysis
@app.route("/api/v1.0/precipitation")

# create a precipitation function
# write a query to get the date and precipitation for the previous year
# use jsonify() to format our results into a JSON structured file
def precipitation():
	prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
	precipitation = session.query(Measurement.date, Measurement.prcp).\
		filter(Measurement.date >= prev_year).all()
	precip = {date: prcp for date, prcp in precipitation}
	return jsonify(precip)
# to view in browser, copy url from running flask in terminal and add
# /api/v1.0/precipitation (full link http://127.0.0.1:5000/api/v1.0/precipitation)

# route for stations
@app.route("/api/v1.0/stations")

# define stations function
# Unravel results into a one-dimensional array using the function 
# np.ravel(), with results as our parameter.
# Next, convert unraveled results into a list with the list function, 
# list(), to convert that array into a list. Then jsonify the list
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# define a route for temperature
@app.route("/api/v1.0/tobs")

# define temperature function
# calculate the date one year ago from the last date in the database
# query the primary station for all the temperature observations from the previous year
# unravel results to 1d array, convert to list, then jsonify
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# define routes for statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# define stats function
# We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None
# create a query to select the minimum, average, and maximum temperatures from our SQLite database. We’ll start by just creating a list called sel
# Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
		filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
	    filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
