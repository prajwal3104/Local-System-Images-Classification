import os

class Config:
    SECRET_KEY = 'your_secret_key'
    UPLOAD_FOLDER = 'app/static/uploads'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    LOGGING_PATH = 'logs'
    LOGGING_LEVEL = 'DEBUG'  # Adjust as needed
