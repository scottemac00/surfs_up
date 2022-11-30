# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# set up the database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect tables from the database into SQLAlchemy
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to database
session = Session(engine)

# Define app for Flask application
app = Flask(__name__)

# define the welcome route (root)
@app.route("/")

# create a function with routes for the data
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

