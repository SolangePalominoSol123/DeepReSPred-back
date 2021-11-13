from app import db

class Request (db.Model):
    idRequest = db.Column(db.String(8), primary_key=True)
    email = db.Column(db.String(255))
    pfamID = db.Column(db.String(7))    
    #sequence = db.Column(db.BLOB)       #In S3 name: seqReq{idRequest}.txt
    #isSequence = db.Column(db.Boolean)
    typeInput = db.Column(db.String(30)) #pfamCode, seqSto, seqFasta, seqOnly
    totalTimeProcess = db.Column(db.Integer) #In milliseconds
    browser = db.Column(db.String(255))
    dateAccess = db.Column(db.DateTime)

    #relationship
    filesxreq = db. relationship("Filexreq")
    idStatus= db.Column('idStatus', db.ForeignKey('statusrequest.idStatus'))
    idAccess = db.Column('idAccess', db.ForeignKey('access.idAccess'))