from flask import render_template, request, redirect, url_for, current_app
from app import app, db
from app.models import Annotation
from app.utils import classify_images, preprocess_image, get_face_embeddings, compare_embeddings

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return redirect(url_for('home'))
        
        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('home'))

        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Load your pre-trained model
            # Example:
            # model = load_pretrained_model('models/your_pretrained_model.h5')

            # Add the new image to the database
            annotation = Annotation(image_path=file_path, person_id='Unknown')
            db.session.add(annotation)
            db.session.commit()

            # Classify images in the folder using annotated data
            annotated_data_folder = 'annotated_data'
            classify_images(annotated_data_folder, Annotation.query.all())

            return redirect(url_for('home'))
    except Exception as e:
        current_app.logger.exception("Error in upload_file route: %s", str(e))
        return "An error occurred."
