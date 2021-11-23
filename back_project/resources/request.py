from app import db
from flask_restful import Resource
from flask import request
from models.request import Request
from models.endpoint import Endpoint
from models.parameter import Parameter
from models.access import Access
from emailconfig import sendEmail
from datetime import datetime
from constants import IP_INFO_TOKEN
from constants import DAEMON_QUEUE_FOLDER
from werkzeug.utils import secure_filename
import os 
import ipinfo

class RequestResource(Resource):
    
    def getEndpointAdditionalData(self, ipClient):      
        handler = ipinfo.getHandler(IP_INFO_TOKEN)
        details = handler.getDetails(ipClient)

        latitude = details.latitude
        longitude = details.longitude
        countryName = details.country_name

        idEndpoint=-1
        active=True
        endpoints = Endpoint.query.filter_by(latitude=latitude,longitude=longitude).all()
        if(len(endpoints)>0):
            idEndpoint=endpoints[0].idEndpoint
            active=endpoints[0].active

        data={
            'idEndpoint' : idEndpoint,
            'latitude' : latitude,
            'longitude' : longitude,
            'countryName' : countryName,
            'active' : active
            }
        return data

    def insertNewEndpoint(self, data):

        endpoint = Endpoint(
            latitude = data['latitude'],
            longitude = data['longitude'],
            countryName = data['countryName'],
            active = True
        )

        db.session.add(endpoint)
        db.session.commit()
        
        response={
            'idEndpoint' : endpoint.idEndpoint,
            'latitude' : endpoint.latitude,
            'longitude' : endpoint.longitude,
            'countryName' : endpoint.countryName,
            'active' : endpoint.active,
        }

        return response
    
    def exceedsDailyRequests(self, idEndpoint, ipClient):
        maxRequests = (Parameter.query.filter_by(idParameter=1).all())[0].value

        #verify if ipClient is registered
        ipClients = Access.query.filter_by(idEndpoint=idEndpoint, ipClient=ipClient).all()

        idAccess = ""
        if(len(ipClients)<=0):
            newAccess = Access(
                idEndpoint = idEndpoint,
                ipClient = ipClient,
                active = True
            )
            db.session.add(newAccess)
            db.session.commit()
            idAccess = newAccess.idAccess
        else:
            accessAux = ipClients[0]
            idAccess = accessAux.idAccess
            """
            if(not accessAux.active):
                data={
                    'idAccess' : accessAux.idAccess,
                    'active' : False,
                    'maxRequests' : maxRequests,
                    'exceed' : False
                }
                return data
            """
        #Til now the ipClient is registered and active
        requests = Request.query.filter_by(idAccess=idAccess).all()
        
        now = datetime.now()
        dateAccessAux = now.strftime("%Y-%m-%d")
        print("Today is:"+dateAccessAux)
        count=0
        for req in requests:
            dateReq=req.dateAccess
            if (dateReq):
                dateReq=dateReq.strftime("%Y-%m-%d")
                print("dateRequestEvaluating")
                if (dateReq==dateAccessAux):
                    count += 1

        accessReq = Access.query.get_or_404(idAccess)
        if count+1>maxRequests:
            exceed=True
            accessReq.active = False
        else:
            exceed=False
            accessReq.active = True

        db.session.commit() #updating access status

        data={
            'idAccess' : idAccess,
            'active' : accessReq.active,
            'maxRequests' : maxRequests,
            'numRequests' : count,
            'exceed' : exceed
        }
        return data

    def post(self):
        request_json = request.get_json()
        '''
        ipClientPort = str(request.headers['Host'])
        pos=ipClientPort.find(":")
        ipClient=ipClientPort[:pos]
        '''
        ipClient = request_json['ipClient']

        #ipClient="190.237.60.38" ############################################## BORRAR
        #ipClient="190.187.147.146" #brigito
        #ipClient="179.6.204.26" #eddie

        endpoint=self.getEndpointAdditionalData(ipClient)
        print(endpoint)
        if (endpoint['idEndpoint']==-1):           
            print("Endpoint not registered")
            newEndpoint = self.insertNewEndpoint(endpoint)
            endpoint['idEndpoint'] = newEndpoint['idEndpoint']

        else:
            
            if (endpoint['active']):

                print("verify number of requests today from ipClient")
                rsp = self.exceedsDailyRequests(endpoint['idEndpoint'], ipClient)

                if (not rsp['active']):
                    print("ipClient access denied")
                    response={
                        'error':True,
                        'errorMsg':"The requests from IP "+ ipClient + " are not allowed. Please try again tomorrow.",
                        'maxRequests' : rsp['maxRequests'],
                        'active' : rsp['active']
                    }
                    return response, 200
                
                if (rsp['exceed']):
                    print("Exceeds Number of Daily Requests")
                    response={
                        'error':True,
                        'errorMsg':"This service only allows a maximum of " + str(rsp['maxRequests']) +" requests per day. Please try again tomorrow.",
                        'maxRequests' : rsp['maxRequests'],
                        'numRequests' : rsp['numRequests'],
                        'exceed' : rsp['exceed']
                    }
                    return response, 200

            else:
                #endPoint bloqueado
                response={
                        'error':True,
                        'errorMsg':"Requests from (" +  endpoint['latitude'] + ", " + endpoint['longitude'] + ") - " + endpoint['countryName']+ " are not allowed",
                        'latitude' : endpoint['latitude'],
                        'longitude' : endpoint['longitude'],
                        'countryName' : endpoint['countryName'],
                        'active' : endpoint['active']
                    }
                return response, 200


        #Register request

        idRequest = request_json['idRequest']
        email = request_json['email']
        pfamID = request_json['pfamID']
        typeInput = request_json['typeInput']


        browser = request.headers['User-Agent']

        now = datetime.now()
        dateAccess = now.strftime("%Y-%m-%d %H:%M:%S")

        idStatus = 1 
        idAccess = rsp['idAccess']

        req = Request(
            idRequest = idRequest,
            email = email,
            pfamID = pfamID,
            typeInput = typeInput,
            browser = browser,
            dateAccess = dateAccess,
            idStatus = idStatus,
            idAccess = idAccess
        )

        db.session.add(req)
        db.session.commit()

        self.createFileDaemon(req.idRequest)

        self.sendConfirmationEmail(email, req.idRequest)
              
        #dateReq=req.dateAccess.strftime("%Y-%m-%d %H:%M:%S")
        response={
            'error':False,
            'idRequest' : req.idRequest,
            'email' : req.email,
            'pfamID' : req.pfamID,
            'typeInput' : typeInput,
            'browser' : req.browser,
            'dateAccess' : dateAccess,
            'idStatus' : req.idStatus,
            'idAccess' : req.idAccess,
            'maxRequests' : rsp['maxRequests'],
            'numRequests' : rsp['numRequests']+1
        }
        return response, 200

    def delete(self):
        request_json = request.get_json()

        id_req = request_json['id']
        req = Request.query.get_or_404(id_req)

        db.session.delete(req)
        db.session.commit()

        response = {
            'error':False,
            'ok': "Request deleted successfully."
        }

        #return response, 204  #204 code doesn't return anything
        return response, 200

    def createFileDaemon(self, idRequest):
        nameFileFull=os.path.join(DAEMON_QUEUE_FOLDER, secure_filename(idRequest))
        text_file = open(nameFileFull, "w")
        text_file.write(idRequest)
        text_file.close()
    
    def sendConfirmationEmail(self, email, idRequest):
        if((email) or (email!="")):
            print("Sending confirmation email")
            sendEmail(email, [], 1, idRequest)

    def put(self):
        request_json = request.get_json()

        idRequest = request_json['idRequest']

        reqAux = Request.query.get_or_404(idRequest)

        if 'email' in request_json:
            email = request_json['email']
            reqAux.email=email

        if 'pfamID' in request_json:
            pfamID = request_json['pfamID']
            reqAux.pfamID=pfamID

        if 'idStatus' in request_json:
            idStatus = request_json['idStatus']
            reqAux.idStatus=idStatus

        if 'totalTimeProcess' in request_json:
            totalTimeProcess = request_json['totalTimeProcess']
            reqAux.totalTimeProcess=totalTimeProcess
        
        db.session.commit()

        response= {
            "idRequest": reqAux.idRequest,
            "email": reqAux.email,
            "pfamID": reqAux.pfamID,
            "idStatus": reqAux.idStatus,
            "totalTimeProcess": reqAux.totalTimeProcess
        }

        return response, 200