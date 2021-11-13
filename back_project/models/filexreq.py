from app import db 

class Filexreq (db.Model):
    idFilexreq=db.Column(db.Integer, primary_key=True)
    isResult = db.Column(db.Boolean)

    #relationship
    idRequest = db.Column('idRequest', db.ForeignKey('request.idRequest'))
    idFile = db.Column('idFile', db.ForeignKey('file.idFile'))