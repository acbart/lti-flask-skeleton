'''
Server administration commands, including running the local development server
and database management.
'''

import sys, os

from main import app
from flask.ext.script import Manager, Server
from scripts.db_commands import ResetDB, PopulateDB, DisplayDB

app.config["SERVER CERTIFICATE FILE"]

context = (app.config["SERVER_CERTIFICATE_FILE"], 
           app.config["SERVER_KEY_FILE"])

manager = Manager(app)

# Server commands context
manager.add_command("secure", Server(ssl_context=context))

# Database Commands
manager.add_command("reset_db", ResetDB())
manager.add_command("populate_db", PopulateDB())
manager.add_command("display_db", DisplayDB())

if __name__ == "__main__":
    manager.run()
