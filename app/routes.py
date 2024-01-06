# routes.py
from flask import render_template, request, redirect, url_for, current_app
from app import app
from app.utils import classify_images

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        current_app.logger.exception("Error in home route: %s", str(e))
        return "An error occurred."

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return redirect(url_for('home'))

        folder_path = "/Users/prajwal/Developer/Local Images Classification/app/static/uploads" # this is the path to your uploaded files
        annotations = []  # You can add annotations if needed

        classify_images(folder_path, annotations)  # Call the classification function

        return "Processing complete!"
    except Exception as e:
        current_app.logger.exception("Error in upload_file route: %s", str(e))
        return "An error occurred."
