from app import db
from flask_restful import Resource
from flask import request
from models.statusrequest import Statusrequest

class StatusrequestResource(Resource):
    def get(self):
        request_json = request.get_json()

        id = request_json['id']
        statusrequest = Statusrequest.query.get_or_404(id)
        response={
            'idStatus' : statusrequest.idStatus,
            'name' : statusrequest.name
        }
        return response, 200

    def get(self):
        statusrequests = Statusrequest.query.all()

        statusrequests_list=[]

        for statusrequest in statusrequests:
            element={
                'idStatus' : statusrequest.idStatus,
                'name' : statusrequest.name
            }
            statusrequests_list.append(element)
        
        response={
            'statusrequests': statusrequests_list
        }

        return response, 200

    def post(self):
        request_json = request.get_json()

        name = request_json['name']

        statusrequest = Statusrequest(name=name)

        db.session.add(statusrequest)
        db.session.commit()

        response={
            'idStatus' : statusrequest.idStatus,
            'name' : statusrequest.name
        }
        return response, 200

    def delete(self):
        request_json = request.get_json()

        id_statusrequest = request_json['id']
        statusrequest = Statusrequest.query.get_or_404(id_statusrequest)

        db.session.delete(statusrequest)
        db.session.commit()

        response = {'ok': "Statusrequest deleted successfully."}

        #return response, 204  #204 code doesn't return anything
        return response, 200

    def put(self):
        request_json = request.get_json()

        idStatus = request_json['idStatus']
        statusrequest = Statusrequest.query.get_or_404(idStatus)

        if 'name' in request_json:
            name = request_json['name']
            statusrequest.name = name

        response={
            'idStatus' : statusrequest.idStatus,
            'name' : statusrequest.name
        }

        db.session.commit()

        return response, 200