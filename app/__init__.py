from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# set up the flask app
app = Flask(__name__)

# point it to the configuration file
app.config.from_object('config')

# create the sqlalchemy connection to the database
db = SQLAlchemy(app)

from app import views, models