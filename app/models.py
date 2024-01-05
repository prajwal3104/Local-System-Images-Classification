from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(100), nullable=False)
    person_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Annotation('{self.image_path}', '{self.person_id}', '{self.timestamp}')"
