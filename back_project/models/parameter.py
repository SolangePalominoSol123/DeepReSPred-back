from app import db 

class Parameter(db.Model):
    idParameter = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(255))
    value = db.Column(db.Integer, nullable=False)