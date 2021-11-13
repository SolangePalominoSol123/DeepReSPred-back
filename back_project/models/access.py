from app import db

class Access (db.Model):
    idAccess = db.Column(db.Integer, primary_key=True)
    ipClient = db.Column(db.String(15))
    active = db.Column(db.Boolean)

    #relaciones
    idEndpoint = db.Column('idEndpoint', db.ForeignKey('endpoint.idEndpoint'))
    requests = db.relationship("Request")