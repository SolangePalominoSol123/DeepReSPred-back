from app import db
from flask_restful import Resource
from flask import request
from models.endpoint import Endpoint

class EndpointResource(Resource):

    def delete(self):
        request_json = request.get_json()

        id_endpoint = request_json['id']
        endpoint = Endpoint.query.get_or_404(id_endpoint)

        db.session.delete(endpoint)
        db.session.commit()

        response = {
            'error' : False,
            'ok': "Endpoint deleted successfully."
        }

        #return response, 204  #204 code doesn't return anything
        return response, 200

    def get(self):
        endpoints = Endpoint.query.all()

        endpoints_list=[]

        for endpoint in endpoints:
            element={
                'idEndpoint' : endpoint.idEndpoint,
                'latitude' : endpoint.latitude,
                'longitude' : endpoint.longitude,
                'countryName' : endpoint.countryName,
                'active' : endpoint.active
            }
            endpoints_list.append(element)
        
        response={
            'error' : False,
            'endpoints': endpoints_list
        }

        return response, 200
    
    def put(self):
        idEndpoint = request_json['idEndpoint']
        endpoint = Endpoint.query.get_or_404(idEndpoint)

        if endpoint.active:
            endpoint.active=False
        else:
            endpoint.active=True

        response={
            'error' : False,
            'idEndpoint' : endpoint.idEndpoint,
            'latitude' : endpoint.latitude,
            'longitude' : endpoint.longitude,
            'countryName' : endpoint.countryName,
            'active' : endpoint.active
        }

        db.session.commit()

        return response, 200

    def enableDisableEndpoint(self, idEndpoint, status):
        endpoint = Endpoint.query.get_or_404(idEndpoint)
        endpoint.active=status

        response={
            'error' : False,
            'idEndpoint' : endpoint.idEndpoint,
            'latitude' : endpoint.latitude,
            'longitude' : endpoint.longitude,
            'countryName' : endpoint.countryName,
            'active' : endpoint.active
        }

        db.session.commit()

        return response, 200