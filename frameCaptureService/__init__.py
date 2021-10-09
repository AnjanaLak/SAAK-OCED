## This process is responsible to capture and store frames from camera #############################################

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app2 = Flask(__name__)  # is a special variable in python that is just the name of the module
# app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/saak.db'  # '///' =>relative path from current directory
# app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app2)
# ma = Marshmallow(app2)

# should import each models here
from mainApp import models

# db.create_all()

# importing routes

from frameCaptureService import frameCaptureRoute
