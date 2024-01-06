from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from config import Config
import os

app = Flask(__name__)
from app.utils import load_facenet_model

model = load_facenet_model(model_url="https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4")
print("FaceNet model loaded successfully.")

from app import routes
