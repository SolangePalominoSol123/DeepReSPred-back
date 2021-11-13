from app import db
from flask_restful import Resource
from flask import request
from models.parameter import Parameter

class ParameterResource(Resource):
    def get(self):
        request_json = request.get_json()

        id = request_json['id']
        parameter = Parameter.query.get_or_404(id)
        response={
            'idParameter' : parameter.idParameter,
            'name' : parameter.name,
            'description' : parameter.description,
            'value' : parameter.value
        }
        return response, 200

    def get(self):
        parameters = Parameter.query.all()

        parameters_list=[]

        for parameter in parameters:
            element={
                'idParameter' : parameter.idParameter,
                'name' : parameter.name,
                'description' : parameter.description,
                'value' : parameter.value
            }
            parameters_list.append(element)
        
        response={
            'parameters': parameters_list
        }

        return response, 200

    def post(self):
        request_json = request.get_json()

        name = request_json['name']
        description = request_json['description']
        value = request_json['value']

        parameter = Parameter(
            name=name,
            description=description,
            value=value
        )

        db.session.add(parameter)
        db.session.commit()

        response={
            'idParameter' : parameter.idParameter,
            'name' : parameter.name,
            'description' : parameter.description,
            'value' : parameter.value
        }
        return response, 200

    def delete(self):
        request_json = request.get_json()

        id_parameter = request_json['id']
        parameter = Parameter.query.get_or_404(id_parameter)

        db.session.delete(parameter)
        db.session.commit()

        response = {'ok': "Parameter deleted successfully."}

        #return response, 204  #204 code doesn't return anything
        return response, 200

    def put(self):
        request_json = request.get_json()


        valueCpu = request_json['cpuNumber']
        valueRequests = request_json['maxRequests']
        valueResidues = request_json['maxResidues']

        parameterReq = Parameter.query.get_or_404(1)
        parameterReq.value=valueRequests

        parameterRes = Parameter.query.get_or_404(2)
        parameterRes.value=valueResidues

        parameterCpu = Parameter.query.get_or_404(3)
        parameterCpu.value=valueCpu

        response= {
            "cpuNumber": parameterCpu.value,
            "maxRequests": parameterReq.value,
            "maxResidues": parameterRes.value
        }

        db.session.commit()

        return response, 200

        """
        idParameter = request_json['idParameter']
        parameter = Parameter.query.get_or_404(idParameter)

        if 'name' in request_json:
            name = request_json['name']
            parameter.name = name
        
        if 'description' in request_json:
            description = request_json['description']
            parameter.description = description
        
        if 'value' in request_json:
            value = request_json['value']
            parameter.value = value

        response={
            'idParameter' : parameter.idParameter,
            'name' : parameter.name,
            'description' : parameter.description,
            'value' : parameter.value
        }

        db.session.commit()

        return response, 200
        """