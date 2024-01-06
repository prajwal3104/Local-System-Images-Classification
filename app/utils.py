# app/utils.py
import os
import shutil
import cv2
from app.models import load_facenet_model  # Correct the import statement
from app import app
from sklearn.metrics.pairwise import cosine_similarity

# Placeholder for preprocessing image function
def preprocess_image(image_path):
    try:
        # Your implementation here (example: resizing the image)
        img = cv2.imread(image_path)
        img = cv2.resize(img, (224, 224))  # Adjust dimensions as needed
        return img
    except Exception as e:
        app.logger.exception("Error in preprocess_image function: %s", str(e))
        return None

# Placeholder for getting face embeddings
def get_face_embeddings(model, image_path):
    try:
        # Load your pre-trained model and obtain face embeddings
        img = preprocess_image(image_path)
        if img is not None:
            img = np.expand_dims(img, axis=0)  # Add batch dimension
            face_embeddings = model.predict(img)
            return face_embeddings
    except Exception as e:
        app.logger.exception("Error in get_face_embeddings function: %s", str(e))
        return None

# Placeholder for comparing face embeddings
def compare_embeddings(reference_embedding, test_embedding):
    try:
        # Your implementation here (example: cosine similarity)
        similarity = cosine_similarity(reference_embedding, test_embedding)[0][0]
        return similarity
    except Exception as e:
        app.logger.exception("Error in compare_embeddings function: %s", str(e))
        return 0.0

# Utility function to classify images
def classify_images(image_folder, annotations):
    try:
        # Load the FaceNet model (loaded globally in app/__init__.py)
        found_match = False

        # Classify images in the folder
        for image_file in os.listdir(image_folder):
            if image_file.endswith('.jpg'):
                image_path = os.path.join(image_folder, image_file)
                face_embeddings = get_face_embeddings(load_facenet_model, image_path)
                if face_embeddings is not None:
                    # Check similarity with each person
                    for reference_embedding in annotations:
                        similarity = compare_embeddings(reference_embedding, face_embeddings)

                        # Set a similarity threshold (adjust as needed)
                        similarity_threshold = 0.8

                        if similarity > similarity_threshold:
                            found_match = True
                            destination_folder = os.path.join(image_folder, 'known_faces')
                            os.makedirs(destination_folder, exist_ok=True)
                            shutil.move(image_path, os.path.join(destination_folder, image_file))
                            break

                    # If no match is found, move to the unknown faces folder
                    if not found_match:
                        destination_folder = os.path.join(image_folder, 'unknown_faces')
                        os.makedirs(destination_folder, exist_ok=True)
                        shutil.move(image_path, os.path.join(destination_folder, image_file))
    except Exception as e:
        app.logger.exception("Error in classify_images function: %s", str(e))
