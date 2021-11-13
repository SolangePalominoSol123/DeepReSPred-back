from app import db
from flask_restful import Resource
from flask import request
from models.request import Request

class SearchPredResource(Resource):
    def post(self):
        request_json = request.get_json()
        idRequest = request_json["idRequest"]

        requests = Request.query.filter_by(idRequest=idRequest).all()

        if len(requests)<=0:
            response={
            'idRequest' : idRequest,
            'idStatus' : 0
            }

            return response, 200
        
   
        idStatus=requests[0].idStatus
        typeInput=requests[0].typeInput
        idRequest=requests[0].idRequest
        email=requests[0].email
        pfamID=requests[0].pfamID

        response={
            'idRequest' : idRequest,
            'email' : email,
            'pfamID' : pfamID,
            'idStatus' : idStatus,
            'typeInput' : typeInput
        }

        return response, 200
