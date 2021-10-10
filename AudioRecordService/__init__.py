# # This process is responsible to capture and store Audio Record Through Routes #####################################

from flask import Flask

app1 = Flask(__name__)  # is a special variable in python that is just the name of the module

# should import each models here
from mainApp import models

# db.create_all()

# importing routes

from AudioRecordService import audioRecordRoute
