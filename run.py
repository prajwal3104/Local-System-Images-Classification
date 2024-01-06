# run.py
from app import app, load_facenet_model
from app import routes

model = load_facenet_model(model_url="https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4")
print("FaceNet model loaded successfully.")
