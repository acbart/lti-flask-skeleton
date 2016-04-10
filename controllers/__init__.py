import os

# Flask tools
from flask import g
from flask_security.core import current_user

# Application specific
from main import app

# Add the current user to the global g object
@app.before_request
def load_user():
    if current_user.is_authenticated():
        g.user = current_user
    else:
        g.user = None
        
# Import any administrative aspects, including your database interface
from admin import admin

# Import security handling stuff
import security 

# Useful routes
import utility

# Below you should import all of your controllers and register their blueprint
from users import users
app.register_blueprint(users)
