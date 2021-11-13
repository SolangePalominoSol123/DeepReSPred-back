from app import db
from flask_restful import Resource
from flask import request
from models.filexreq import Filexreq
from models.file import File

class FilexReqInfoResource(Resource):

    def get(self):
        request_json = request.get_json()

        idRequest = request_json['idRequest']
        infoFilesxReq=db.session.query(Filexreq.isResult,Filexreq.idFile,Filexreq.idRequest, File.idSubGroup, File.nameFile).filter(Filexreq.idFile==File.idFile).filter(Filexreq.idRequest==idRequest).filter(Filexreq.isResult==False).filter(File.idSubGroup==0).all()
        print(infoFilesxReq)

        response={
                "idRequest":idRequest,
                "error":True,
                "msgError":"No files encountered"
            }

        if len(infoFilesxReq)>0:
            response={
                "isResult":infoFilesxReq[0].isResult,
                "idFile":infoFilesxReq[0].idFile,
                "idRequest":infoFilesxReq[0].idRequest,
                "idSubGroup":infoFilesxReq[0].idSubGroup,
                "nameFile":infoFilesxReq[0].nameFile,
                "error":False
            }

        return response, 200

    def post(self):
        request_json = request.get_json()
        idRequest = request_json['idRequest']
        idSubGroup = request_json['idSubGroup']
        haveStructure = request_json['haveStructure']
        extension = request_json['extension']
        isFragment = request_json['isFragment']
        dbAlgorithm = request_json['dbAlgorithm']
        isResult = request_json['isResult']
        tmscore = request_json['tmscore']

        newFile=File(
            idSubGroup=idSubGroup,
            haveStructure=haveStructure,
            extension=extension,
            isFragment=isFragment,
            dbAlgorithm=dbAlgorithm,
            tmscore=tmscore
        )

        db.session.add(newFile)
        db.session.commit()

        nameFile="file"+str(newFile.idFile)+"_"+str(newFile.idSubGroup)+newFile.extension
        newFile.nameFile=nameFile
        db.session.commit()

        newFilexReq=Filexreq(
            isResult=isResult,
            idRequest= idRequest,
            idFile=newFile.idFile
        )

        db.session.add(newFilexReq)
        db.session.commit()

        response={
            'idFile' : newFile.idFile,
            'nameFile' : newFile.nameFile,
            'idSubGroup' : newFile.idSubGroup,
            'haveStructure' : newFile.haveStructure,
            'tmscore' : float(newFile.tmscore),
            'extension' : newFile.extension,
            'isFragment' : newFile.isFragment,
            'dbAlgorithm' : newFile.dbAlgorithm,
            'idFilexreq': newFilexReq.idFilexreq
        }
        return response, 200

