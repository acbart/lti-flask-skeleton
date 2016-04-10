'''
This file exposes three useful decorators for your controllers:
    @admin_required
    @instructor_required
    @login_required
    
As you can guess, they will force a user to meet the requirement, or they will
    be redirected to the security login page.
'''

# Built-in imports
from datetime import timedelta
from functools import wraps, update_wrapper
import calendar, datetime
import json

# Flask imports
from flask import g, request, redirect, url_for, make_response, current_app
from flask import flash

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('security.login', next=request.url))
        if not g.user.is_admin():
            flash("This portion of the site is only for administrators.")
            return redirect(url_for('users.index'))
        return f(*args, **kwargs)
    return decorated_function

def instructor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('security.login', next=request.url))
        if not g.user.is_instructor():
            flash("This portion of the site is only for instructors.")
            return redirect(url_for('users.index'))
        return f(*args, **kwargs)
    return decorated_function

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('security.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
