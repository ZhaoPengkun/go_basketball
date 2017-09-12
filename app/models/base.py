from flask import current_app
from flask_sqlalchemy import SQLAlchemy
# from influxdb import InfluxDB

db = SQLAlchemy()
influx_db = None