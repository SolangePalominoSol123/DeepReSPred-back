from app import db

class Statusrequest (db.Model):
    idStatus = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    request = db.relationship("Request")