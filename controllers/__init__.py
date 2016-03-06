import os

from main import app

from models.models import db, User, Role
from flask import session, g, send_from_directory, request, jsonify, render_template
from flask import redirect, url_for
from flask_security.core import current_user

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
