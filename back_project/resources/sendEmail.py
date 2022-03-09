from werkzeug.utils import secure_filename
from app import db
from flask_restful import Resource
from flask import request
from emailconfig import sendEmail
from constants import FILES_DOWNLOADED
from models.request import Request
from models.filexreq import Filexreq
from models.file import File
import pandas as pd
import shutil
import wget
import ssl
import os

class SendEmailResource(Resource):
    """
    def post(self):
        request_json = request.get_json()

        listFilesLocal = request_json['listFilesLocal']
        email = request_json['email']
        idRequest = request_json['idRequest']
        inputType = request_json['inputType']
        inputContent = request_json['inputContent']

        sendEmail(email, listFilesLocal, 2, idRequest, inputType, inputContent)

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
    """
    def clearDir(self, directory):
        try:
            shutil.rmtree(directory)
        except OSError as e:
            print("Error: %s: %s" % (directory, e.strerror))

    def createDir(self, directory):
        isdir = os.path.isdir(directory) 
        if isdir:
            self.clearDir(directory)
        try:
            os.makedirs(directory)
        except:
            print("Error with directory: "+directory)
            return False
        
        return True

    def consultingDB(self, idRequest):

        infoFilesFasta=db.session.query(File.nameFile,File.isFragment, File.idSubGroup).filter(Filexreq.idFile==File.idFile).filter(File.extension=='.fasta').filter(Filexreq.idRequest==idRequest).all()
        infoFilesPDB=db.session.query(File.nameFile,File.isFragment, File.idSubGroup).filter(Filexreq.idFile==File.idFile).filter(File.extension=='.pdb').filter(Filexreq.idRequest==idRequest).all()
        requests = Request.query.filter_by(idRequest=idRequest).all()

        listFilesReport = []
        if(len(requests)>0):
            #typeInput=requests[0].typeInput
            pfamID=requests[0].pfamID

            for elementFasta in infoFilesFasta:
                subGroupFasta = elementFasta.idSubGroup
                for elementPdb in infoFilesPDB:
                    subGroupPDB = elementPdb.idSubGroup
                    if subGroupFasta==subGroupPDB:
                        record={
                            'pfamID' : pfamID,
                            'idRequest' : idRequest,
                            'subgroup' : subGroupPDB,
                            'fasta' : elementFasta.nameFile,
                            'pdb' : elementPdb.nameFile,
                            'isPfamFragment' : elementFasta.isFragment
                        }
                        listFilesReport.append(record)
                        break

        df=pd.DataFrame(listFilesReport)
        return df

    def downloadingResults(self, filename, format, destinationName):
        urlS3='http://54.156.135.177:9997/api/s3file/?code='+filename+'&ext='+format+'&typed=1'
        ssl._create_default_https_context = ssl._create_unverified_context
        wget.download(urlS3, out=destinationName) 
        return destinationName

    def gettingReportResults(self, requestInput, inputType, inputContent):
        
        dfMainData=self.consultingDB(requestInput)
        lenRows=len(dfMainData.index)
        
        nameDir=""
        if(inputType=="pfamCode"):
            nameDir = inputContent+"_idReq"
        else:
            nameDir = "noPfamType_idReq"

        if(lenRows>0):
            nameDir = nameDir + requestInput
        else:
            nameDir = nameDir + requestInput + "_noResults"

        currentDir = FILES_DOWNLOADED
        mainDir = os.path.join(currentDir, secure_filename(nameDir))
        self.createDir(mainDir)

        if(lenRows<=0):
            return

        #fasta dataframe
        dfAuxFasta=dfMainData[['subgroup','fasta']].copy()
        dfAuxFasta = dfAuxFasta.assign(FullNameFile = lambda x: (mainDir+"/"+x["subgroup"].apply(str)+ "_"+ x["fasta"].apply(str)) )
        dfAuxFasta[['NameFile','Format']]=dfAuxFasta.fasta.str.split('.',expand=True)


        #pdb dataframe
        dfAuxPDB=dfMainData[['subgroup','pdb']].copy()
        dfAuxPDB = dfAuxPDB.assign(FullNameFile = lambda x: (mainDir+"/"+x["subgroup"].apply(str)+ "_"+ x["pdb"].apply(str)) )
        dfAuxPDB[['NameFile','Format']]=dfAuxPDB.pdb.str.split('.',expand=True)

        #downloading pdb files

        dfAuxPDB = dfAuxPDB.reset_index()  # make sure indexes pair with number of rows
        for index, row in dfAuxPDB.iterrows():
            pNameFile = row['NameFile']
            pFormat = row['Format']
            pFullNameFile = row['FullNameFile']
            self.downloadingResults(pNameFile, pFormat, pFullNameFile)

        #downloading fasta files

        dfAuxFasta = dfAuxFasta.reset_index()  # make sure indexes pair with number of rows
        for index, row in dfAuxFasta.iterrows():
            pNameFile = row['NameFile']
            pFormat = row['Format']
            pFullNameFile = row['FullNameFile']
            self.downloadingResults(pNameFile, pFormat, pFullNameFile)

        contentFastaTitle=[]
        for index, row in dfAuxFasta.iterrows():
            pFullNameFile = row['FullNameFile']

            fileFasta = open(pFullNameFile, 'r')
            firstLine = fileFasta.readline()
            contentFastaTitle.append(firstLine)

        dfMainData['fragmento'] = contentFastaTitle

        nameExcel=""
        if(inputType=="pfamCode"):
            nameExcel = inputContent
        else:
            nameExcel = "noPfamType"

        #export data to excel
        fullNameFileExcel = os.path.join(mainDir, secure_filename(nameExcel+".xlsx"))
        dfMainData.to_excel(fullNameFileExcel, sheet_name = nameExcel, index = False)

        return mainDir

    def sendEmailWithResults2(self, idRequest, email, inputType, inputContent):
        #it will get fasta files, pdb files and the excel report

        mainDir = self.gettingReportResults(idRequest, inputType, inputContent)

        filesReport_list = os.listdir(mainDir)

        filesFull=[]
        for fileAux in filesReport_list:
            fullPathDownloaded= os.path.join(mainDir, secure_filename(fileAux))
            if fullPathDownloaded!="":
                filesFull.append(fullPathDownloaded)

        #downloadedFiles
        sendEmail(email, filesFull, 2, idRequest, inputType, inputContent)
        self.createDir(FILES_DOWNLOADED)

    def post(self):
        request_json = request.get_json()

        email = request_json['email']
        idRequest = request_json['idRequest']
        inputType = request_json['inputType']
        inputContent = request_json['inputContent']

        self.sendEmailWithResults2(idRequest, email, inputType, inputContent)