from app import db

class Endpoint (db.Model):
    idEndpoint = db.Column(db.Integer, primary_key=True)
    countryName = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    active = db.Column(db.Boolean)

    #requests = db.relationship("Request")
    accesses = db.relationship("Access")