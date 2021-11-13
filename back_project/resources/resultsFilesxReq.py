from app import db
from flask_restful import Resource
from flask import request
from models.filexreq import Filexreq
from models.file import File
from models.request import Request

class ResultsFilesxReq(Resource):

    def get(self):
        request_json = request.get_json()

        idRequest = request_json['idRequest']
        infoFilesxReq=db.session.query(Filexreq.idFile,Filexreq.idRequest, File.idSubGroup, File.isFragment, File.nameFile, File.dbAlgorithm,File.tmscore).filter(Filexreq.idFile==File.idFile).filter(Filexreq.idRequest==idRequest).filter(Filexreq.isResult==True).filter(Request.idStatus==4).filter(Request.idRequest==Filexreq.idRequest).all()
        print(infoFilesxReq)

        files_list=[]
        for filexReq in infoFilesxReq:

            element={
                "idFile":filexReq.idFile,
                "idRequest":filexReq.idRequest,
                "idSubGroup":filexReq.idSubGroup,
                "isFragment":filexReq.isFragment,
                "nameFile":filexReq.nameFile,
                "dbAlgorithm":filexReq.dbAlgorithm
            }

            files_list.append(element)
            
        response={
            "files": files_list
        }
        return response, 200