from app import db
from flask_restful import Resource
from flask import request
from models.request import Request
import shortuuid

class IdRequestResource (Resource):
    def get(self):
        shortID=""
        #create id and verify if already exists in DB
        while True:
            shortID = shortuuid.ShortUUID(alphabet="123456789ABCDEFGHJKLMNPQRSTUVWXYZ").random(length=8)
            requests = Request.query.filter_by(idRequest=shortID).all()
            cantReq=len(requests)
            if cantReq==0:
                break

        response={
            'newId' : shortID
        }
        return response, 200

    def post(self):
        existsID=True

        request_json = request.get_json()
        id = request_json['id']
        requests = Request.query.filter_by(idRequest=id).all()

        if len(requests)==0:
            existsID=False
            recommendedID=id
        else:
            while True:
                shortID = shortuuid.ShortUUID(alphabet="123456789ABCDEFGHJKLMNPQRSTUVWXYZ").random(length=8)
                requests = Request.query.filter_by(idRequest=shortID).all()
                cantReq=len(requests)
                if cantReq==0:
                    break

            recommendedID=shortID

        response={
            'idRequested' : id,
            'existsID' : existsID,
            'recommendedID' : recommendedID
        }
        return response, 200
