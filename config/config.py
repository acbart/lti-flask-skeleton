"""
Flask Configuration File
"""
import os
import yaml

try:
    with open('secrets.yaml', 'r') as secret_file:
        secrets = yaml.load(secret_file)
except IOError:
    print("No secret file found. Create your own secret file based on 'config/example-secrets.yaml'.")
    raise SystemError()

class Config(object):
    # TODO: it is up to you to decide when to increment version numbers
    VERSION = '0.1.0'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    # TODO: e.g., "BlockPy"
    SITE_NAME = 'YOUR APPLICATION NAME GOES HERE'
    # TODO: e.g., "acbart@vt.edu"
    SYS_ADMINS = ['admin@org.extension']
    ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIRECTORY = os.path.join(ROOT_DIRECTORY, 'static')
    BLOCKLY_LOG_DIR = os.path.join(ROOT_DIRECTORY, 'logs')
    
    # secret key for flask authentication
    SECRET_KEY = secrets['FLASK_SECRET_KEY']
    
    # Configure server oauth settings
    SERVER_CERTIFICATE_FILE = secrets['SERVER_CERTIFICATE_FILE']
    SERVER_KEY_FILE = secrets['SERVER_KEY_FILE']
    
    # Configure PyLTI oauth settings
    PYLTI_CONFIG = {
        "consumers": {
            secrets["CONSUMER_KEY"]: {
                "secret": secrets["CONSUMER_KEY_SECRET"],
                "cert": secrets["CONSUMER_KEY_PEM_FILE"]
            }
        }
    }
    
    #configured for GMAIL
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # TODO: e.g., vt.blockpy@gmail.com
    MAIL_USERNAME = 'your_account@gmail.com'
    MAIL_PASSWORD = secrets.get("EMAIL_PASSWORD")
    # TODO: e.g., "BlockPy Admin"
    DEFAULT_MAIL_SENDER = 'Name of the email sender'
    
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = secrets.get('SECURITY_PASSWORD_SALT')
    SECURITY_DEFAULT_REMEMBER_ME = True

    
class ProductionConfig(Config):
    DEBUG = False
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    
class TestingConfig(Config):
    DEBUG = True
    PORT = 5001
    HOST = 'localhost'
    SITE_ROOT_URL = 'localhost:5001'
    # TODO: set your database URI, e.g., for MySQL or PostGres
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
