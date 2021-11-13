from app import db
from flask_restful import Resource
from flask import request
from models.filexreq import Filexreq
from models.request import Request

class ExistsPFAMreqResource(Resource):

    def get(self):
        request_json = request.get_json()

        pfamID = request_json['pfamID']
        idRequest = request_json['idRequest']

        #infoFilesxReq=db.session.query(Filexreq.isResult,Filexreq.idFile,Filexreq.idRequest, Request.pfamID, Request.idStatus, Request.totalTimeProcess).filter(Request.pfamID==pfamID).filter(Filexreq.idRequest!=idRequest).filter(Filexreq.idRequest==Request.idRequest).filter(Filexreq.isResult==True).filter(Request.idStatus==4).distinct().all()
        reqsFounded=db.session.query(Request.idRequest, Request.totalTimeProcess).filter(Request.idStatus==4).filter( Request.pfamID==pfamID).filter( Request.idRequest!=idRequest).all()

        print("Exists this requests with same PFAM ID:")
        print(reqsFounded)

        if len(reqsFounded)>0:
            
            total_seconds=reqsFounded[0].totalTimeProcess
            idRequest_Aux=reqsFounded[0].idRequest

            reqAux=Request.query.get_or_404(idRequest)

            reqAux.totalTimeProcess=total_seconds
            reqAux.idStatus=4
            db.session.commit()

            infoFilesxReq=db.session.query(Filexreq.idFile).filter(Filexreq.idRequest==idRequest_Aux).filter( Filexreq.isResult==True).all()
            for infoFileAux in infoFilesxReq:
                
                newFilexReq=Filexreq(
                    isResult=True,
                    idFile=infoFileAux.idFile,
                    idRequest=idRequest
                )

                db.session.add(newFilexReq)
                db.session.commit()

            response={
                "result":True
            }
        else:
            response={
                "result":False
            }


        return response, 200