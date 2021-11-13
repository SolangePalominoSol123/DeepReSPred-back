from app import db
from flask_restful import Resource
from datetime import datetime
from models.endpoint import Endpoint
from models.request import Request
from models.access import Access
from flask import request
import pandas as pd

class AccessResource(Resource):

    def setStatus(self, x):
        status="ENABLED"
        if(not x):
            status="DISABLED"
        return status

    def processDataAccesses(self, listAccesses):

        if (len(listAccesses)<=0):
            return []
            
        dfIni = pd.DataFrame(listAccesses, columns =['countryName','ipClient','active','dateTime', 'date','browser'])
        dfBrowsers=dfIni[["dateTime","browser","active","countryName"]]

        dfReq=dfIni.groupby(['ipClient']).count()
        dfReq=pd.DataFrame(dfReq, columns =['active'])
        dfReq.reset_index(level=0, inplace=True)
        dfReq.rename(columns = {'active': 'nRequests'}, inplace = True)

        dfDatesMax=dfIni[['ipClient','dateTime']]
        dfDatesMax=dfDatesMax.groupby(['ipClient']).max()
        dfDatesMax.reset_index(level=0, inplace=True)

        mergedDetails = pd.merge(left=dfDatesMax, right=dfBrowsers, left_on='dateTime', right_on='dateTime')
        mergedDetails['active'] = mergedDetails['active'].apply(self.setStatus)
        mergedDetails.rename(columns = {'active': 'status'}, inplace = True)

        mergeComplete = pd.merge(left=mergedDetails,right=dfReq,left_on="ipClient",right_on="ipClient")
        mergeComplete.rename(columns = {'dateTime': 'lastAccess'}, inplace = True)

        return mergeComplete.values.tolist()

    def post(self):
        request_json = request.get_json()

        status = request_json['status']
        ipSearch = request_json['ipSearch']

        correctStatus=[]
        if(status=="GENERAL"):
            correctStatus=["ENABLED","DISABLED"]
        else:
            correctStatus.append(status)

        accesses=db.session.query(Endpoint.countryName, Access.ipClient, Access.active, Request.dateAccess, Request.browser).filter(Endpoint.idEndpoint==Access.idEndpoint).filter(Request.idAccess==Access.idAccess).order_by(Request.dateAccess.desc()).all()

        today = (datetime.now()).strftime("%Y-%m-%d")

        list_accesses=[]
        for access in accesses:
            element=[]
            dateReq=access[3].strftime("%Y-%m-%d")
            if (dateReq==today):
                element.append(access[0])
                element.append(access[1])
                element.append(access[2])
                element.append(access[3].strftime("%Y-%m-%d %H:%M:%S"))
                element.append(dateReq)
                element.append(access[4])

                list_accesses.append(element)

        processedList = self.processDataAccesses(list_accesses)

        orderedList=[]
        for accessAux in processedList:
            element={
                'IPClient':accessAux[0],
                'browser':accessAux[2],
                'lastAccess':accessAux[1],
                'numRequests':accessAux[5],
                'countryName':accessAux[4],
                'status':accessAux[3]
            }

            posIP=1
            if ipSearch!="":
                posIP=element["IPClient"].find(ipSearch)

            if ((element["status"] in correctStatus) and(posIP>=0)):
                orderedList.append(element)

        response={
            "accesses": orderedList
        }
        return response,200
