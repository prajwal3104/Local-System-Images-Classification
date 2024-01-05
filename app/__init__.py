from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Configure logging
if not app.debug:
    if not os.path.exists(app.config['LOGGING_PATH']):
        os.makedirs(app.config['LOGGING_PATH'])

    log_file_path = os.path.join(app.config['LOGGING_PATH'], 'app.log')
    handler = RotatingFileHandler(log_file_path, maxBytes=10240, backupCount=10)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    handler.setLevel(app.config['LOGGING_LEVEL'])
    app.logger.addHandler(handler)

db = SQLAlchemy(app)

from app import routes
