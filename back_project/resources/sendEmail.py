from app import db
from flask_restful import Resource
from flask import request
from emailconfig import sendEmail
from constants import FILES_DOWNLOADED
import os
import shutil

class SendEmailResource(Resource):
    def post(self):
        request_json = request.get_json()

        listFilesLocal = request_json['listFilesLocal']
        email = request_json['email']
        idRequest = request_json['idRequest']

        sendEmail(email, listFilesLocal, 2, idRequest)

        try:
            shutil.rmtree(FILES_DOWNLOADED)
            isdir = os.path.isdir(FILES_DOWNLOADED) 
            if not isdir:        
                try:
                    os.makedirs(FILES_DOWNLOADED)
                except:
                    print("Error with directory: "+FILES_DOWNLOADED)

        except OSError as e:
            print("Error: %s: %s" % (FILES_DOWNLOADED, e.strerror))

        response={
            'error' : False
        }
        return response, 200