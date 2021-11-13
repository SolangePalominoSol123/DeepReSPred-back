from app import db
from flask_restful import Resource
from flask import request
from models.file import File
from models.filexreq import Filexreq

from constants import BUCKET_NAME
from constants import UPLOAD_FOLDER
from s3config import getS3config
import os 
from werkzeug.utils import secure_filename

class FileResource(Resource):

    def delete(self):
        request_json = request.get_json()

        idFile = request_json['id']
        fileAux = File.query.get_or_404(idFile)

        filesXReqs = Filexreq.query.filter_by(idFile=idFile).all()
        for filexreq in filesXReqs:
            db.session.delete(filexreq)

        db.session.delete(fileAux)
        db.session.commit()

        response = {'ok': "File and relations deleted successfully."}

        #return response, 204  #204 code doesn't return anything
        return response, 200

    def get(self):
        files = File.query.all()

        files_list=[]

        for fileAux in files:
            element={
                'idFile' : fileAux.idFile,
                'idSubGroup' : fileAux.idSubGroup,
                'haveStructure' : fileAux.haveStructure,
                'content' : fileAux.content,
                'extension' : fileAux.extension,
                'isFragment' : fileAux.isFragment
            }
            files_list.append(element)
        
        response={
            'error': False,
            'files': files_list
        }

        return response, 200
    
    def post(self):
        print("post file")
        
        filename=request.form["filename"]
        extension=request.form["extension"]
        dataFile=request.form["data"]
        idRequest=request.form["idRequest"]
        
        print(filename)
        print(extension)
        #print(dataFile)
        print(idRequest)
        
        """
        f = request.files['file']
        print(f)
        dirAux=os.path.join(UPLOAD_FOLDER, secure_filename(f.filename))
        f.save(dirAux)
        
        """
        #Registering file in DB
        inputFile = File(
            idSubGroup = 0,  #In case is an input files
            nameFile = "",   #In S3 name: file{idFile}_{idSubGroup}.{extension}
            extension = extension,
            dbAlgorithm = "PFAM"
        )
        db.session.add(inputFile)
        db.session.commit()

        newNameFile = "file" + str(inputFile.idFile) + "_0" + inputFile.extension
        inputFile.nameFile = newNameFile
        db.session.commit()

        #Registering relation request x file in DB
        inputFilexReq = Filexreq(
            isResult = False,
            idRequest = idRequest,
            idFile = inputFile.idFile
        )
        
        db.session.add(inputFilexReq)
        db.session.commit()

        nameFile=newNameFile
        data = self.data2File(nameFile, dataFile)
        
   
        if (data[0]):
            ###### upload_file(f"uploads/{f.filename}", BUCKET)

            s3_client=getS3config()
            response = s3_client.upload_file(data[1], BUCKET_NAME, newNameFile)
            
        else:
            response ={
                'error': True,
                'errorMsg': "Ocurrió un error al crear el archivo en local"
            }
      
        return response, 200

    def data2File (self, nameFile, data):

        isdir = os.path.isdir(UPLOAD_FOLDER)             
        if not isdir:        
            try:
                os.makedirs(UPLOAD_FOLDER)
            except:
                print("Error with directory: "+UPLOAD_FOLDER)
                return (False, "")
        
        nameFileFull=os.path.join(UPLOAD_FOLDER, secure_filename(nameFile))

        text_file = open(nameFileFull, "w")
        text_file.write(data)
        text_file.close()
        return (True, nameFileFull)
 
    def generateAllLinkFiles(self):
        s3_client = getS3config()
        public_urls = []
        count=0
        try:
            for item in s3_client.list_objects(Bucket=BUCKET_NAME)['Contents']:
                if count==0:
                    print(item)
                presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': BUCKET_NAME, 'Key': item['Key']}, ExpiresIn = 100)
                public_urls.append(presigned_url)
                count+=1
        except Exception as e:
            pass
        
        #print("[INFO] : The contents inside show_image = ", public_urls)
        return public_urls
    
    def generateLinkFile(self, filename):
        s3_client = getS3config()
        try:            
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': BUCKET_NAME, 'Key': filename}, ExpiresIn = 150)
        except Exception as e:
            pass
        
        print("[INFO] : The contents inside show_image = ", presigned_url)
        return presigned_url