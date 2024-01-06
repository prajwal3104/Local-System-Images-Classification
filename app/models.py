# app/models.py
import tensorflow as tf
import tensorflow_hub as hub

def load_facenet_model(model_url):
    model = tf.keras.Sequential([
        hub.KerasLayer(model_url, input_shape=(224, 224, 3))
    ])
    return model
