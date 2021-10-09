######## related to port 3 ###################################

import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app3 = Flask(__name__)  # is a special variable in python that is just the name of the module
app3.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/saak.db'  # '///' =>relative path from current directory
app3.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app3)
ma = Marshmallow(app3)

# should import each models here
#from mainApp import models
from preview import camPreview

db.create_all()

# importing routes

from preview import previewRoute
