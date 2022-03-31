from app import db
from flask_restful import Resource
from flask import request
from flask import current_app as app
from flask import send_file,send_from_directory

from constants import BUCKET_NAME
from constants import S3_UPLOAD_DIR
from constants import FILES_DOWNLOADED
from s3config import getS3config
import os 
from werkzeug.utils import secure_filename

class S3FileResource(Resource):

    def post(self):
        #Subir a S3 un archivo que ya esta en local
        request_json = request.get_json()

        name = request_json['name']
        extension = request_json['extension']
        response=self.post2s3(name, extension)

        #response = {'ok': "File and relations deleted successfully."}
        return response, 200
    
    def post2s3(self, name, extension):
        
        fullNamePath=os.path.join(S3_UPLOAD_DIR, secure_filename(name+extension))

        s3_client=getS3config()
        response = s3_client.upload_file(fullNamePath, BUCKET_NAME, secure_filename(name+extension))
     
        return response

    
    def get(self):       
        #descargar de s3
        print(request)
        code = request.args['code']
        extension = request.args['ext']
        typeDownload = request.args['typed'] #1:as attachment, 0:just locally

        fullName=secure_filename(code+"."+extension)
        print("s3: "+fullName)
        fullNamePath=os.path.join(FILES_DOWNLOADED, fullName)
        s3_client=getS3config()
        #brindar info
        try:
            s3_client.download_file(BUCKET_NAME, fullName, fullNamePath)  

            if(typeDownload=="1"):
                print("es 1")
                resp=send_from_directory(FILES_DOWNLOADED, filename=fullName, as_attachment=True)
        except Exception as e:
            print("File not found")
            print(e)
            response={
                    "error":True
                }
            return response, 200

        #borrar del entorno local
        print(fullNamePath)
        if os.path.exists(fullNamePath):
            if (typeDownload=="1"):
                os.remove(fullNamePath)
                print("File deleted")
                return resp
            else:
                response={
                    "error":False,
                    "fullNamePath":fullNamePath
                }
                return response,200

        response={
                "error":True
            }
        return response, 200
