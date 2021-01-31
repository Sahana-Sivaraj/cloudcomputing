# application1/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()
class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(255), unique=True, nullable=False)
    healthy = db.Column(db.Integer, nullable=False)

    def __init__(self, name, location, healthy):
        self.name = name
        self.healthy = healthy
        self.location = location

    def __repr__(self):
        return '<Students %r>' % self.StudentID

    def get_id(self):
        return str(self.StudentID)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'healthy': self.healthy
        }
