'''
Main flask application, run by your WSGI file. Note that this is not the main
point of entry for running your server locally; that distinction belongs to your
manage.py file.
'''

# System imports
import os
import sys
import logging

# Flask imports
from flask import Flask

# Initially build the flask appliation
app = Flask(__name__)

# Log any information from the application to the console
# You might consider modifying this (e.g., log to a file instead)
LOGGING_LEVEL = logging.INFO
root = logging.getLogger('SystemLogger')
root.setLevel(LOGGING_LEVEL)
channel = logging.StreamHandler(sys.stdout)
channel.setLevel(LOGGING_LEVEL)
formatter = logging.Formatter('%(name)s[%(levelname)s] - %(message)s')
channel.setFormatter(formatter)
root.addHandler(channel)

# Load in your application configuration
# TODO: switch to config.ProductionConfig for the production server
app.config.from_object('config.config.TestingConfig')

# Assign the VERSION to this application.
VERSION = app.config['VERSION']

# Your controllers
import controllers
