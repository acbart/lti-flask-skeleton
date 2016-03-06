import os

# Flask tools
from flask_security.core import current_user

# Application specific
from main import app

@app.before_request
def load_user():
    if current_user.is_authenticated():
        g.user = current_user
    else:
        g.user = None
        
# Below you should import all of your controllers and potentially register them

from admin import admin

import security 

import utility

from users import users
app.register_blueprint(users)
