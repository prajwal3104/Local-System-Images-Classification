import os

def create_directory_structure(project_root):
    # Create main project directory
    os.makedirs(project_root, exist_ok=True)

    # Create app directory and subdirectories
    app_path = os.path.join(project_root, 'app')
    os.makedirs(app_path, exist_ok=True)

    static_path = os.path.join(app_path, 'static')
    os.makedirs(static_path, exist_ok=True)

    uploads_path = os.path.join(static_path, 'uploads')
    os.makedirs(uploads_path, exist_ok=True)

    templates_path = os.path.join(app_path, 'templates')
    os.makedirs(templates_path, exist_ok=True)

    # Create files within the app directory
    create_file(os.path.join(app_path, '__init__.py'))
    create_file(os.path.join(app_path, 'models.py'))
    create_file(os.path.join(app_path, 'routes.py'))
    create_file(os.path.join(app_path, 'utils.py'))

    # Create virtual environment directory
    os.makedirs(os.path.join(project_root, 'venv'), exist_ok=True)

    # Create other project files
    create_file(os.path.join(project_root, '.gitignore'), '*.pyc\n*.pyo\n__pycache__/\nvenv/\n*.db')
    create_file(os.path.join(project_root, 'config.py'), 'class Config:\n    SECRET_KEY = \'your_secret_key\'\n    UPLOAD_FOLDER = \'app/static/uploads\'\n    SQLALCHEMY_DATABASE_URI = \'sqlite:///site.db\'')
    create_file(os.path.join(project_root, 'requirements.txt'), 'Flask\nFlask-SQLAlchemy\nnumpy\nopencv-python\nscikit-learn\ntensorflow')
    create_file(os.path.join(project_root, 'run.py'), 'from app import app\n\nif __name__ == "__main__":\n    app.run(debug=True)')

def create_file(file_path, content=''):
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    create_directory_structure('Local Images Classification')
