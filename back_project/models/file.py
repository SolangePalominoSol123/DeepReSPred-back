from app import db 

class File (db.Model):
    idFile = db.Column(db.Integer, primary_key=True)
    idSubGroup = db.Column(db.Integer)      #0: when it is input
    haveStructure = db.Column(db.Boolean, default=False)   #Flag of comparation file (the sequence with PDB structures also are saved)
    nameFile = db.Column(db.String(255))    #In S3 name: file{idFile}_{idSubGroup}.{extension}
    extension = db.Column(db.String(10))
    isFragment = db.Column(db.Boolean, default=False)      #Flag to identify is the file is related to a complete sequence or a fragment
    dbAlgorithm = db.Column(db.String(25))  #Database used to create intermediate files to use algorithm: UniRef30_2020_06, PFAM
    tmscore = db.Column(db.Numeric(4,3), default=0)

    filesxreq = db. relationship("Filexreq")