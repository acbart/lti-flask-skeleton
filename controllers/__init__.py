import os

# Flask tools
from flask import g
from flask_security.core import current_user

# Application specific
from main import app

# Add the current user to the global g object
@app.before_request
def load_user():
    if current_user.is_authenticated:
        g.user = current_user
        if 'lti_course' in session:
            g.course = Course.by_id(session['lti_course'])
    else:
        g.user = None
        
# Import any administrative aspects, including your database interface
from controllers.admin import admin

# Import security handling stuff
import controllers.security 

# Useful routes
import controllers.utility

# Below you should import all of your controllers and register their blueprint
# ...

@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello world!"
