from app import db
from flask_restful import Resource
from flask import request
from models.filexreq import Filexreq
from models.file import File

class AllFilesxReq(Resource):

    def post(self):
        request_json = request.get_json()

        idRequest = request_json['idRequest']
        infoFilesxReq=db.session.query(Filexreq.isResult, File.idSubGroup, Filexreq.idFile,Filexreq.idRequest, File.nameFile, File.tmscore, File.extension).filter(Filexreq.idFile==File.idFile).filter(Filexreq.idRequest==idRequest).all()
        print(infoFilesxReq)

        filesInput=[]
        filesMiddle=[]
        filesResult=[]

        for fileFinded in infoFilesxReq:
            element={
                "nameFile":fileFinded.nameFile,
                "extension":fileFinded.extension,
                "tmscore":float(fileFinded.tmscore),
                "isResult":fileFinded.isResult,
                "idSubGroup":fileFinded.idSubGroup,
                "idFile":fileFinded.idFile,
                "idRequest":fileFinded.idRequest               
            }

            if fileFinded.isResult:
                filesResult.append(element)
            elif (not fileFinded.isResult) and (fileFinded.idSubGroup==0):
                filesInput.append(element)
            else:
                filesMiddle.append(element)

        
        response={
            "filesInput":filesInput,
            "filesMiddle":filesMiddle,
            "filesResult":filesResult
        }

        return response, 200