from Bio import SeqIO
import os
import requests
import shutil
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from constants import FILES_DOWNLOADED
from constants import URL_BACK_END_DEEPRESPRED
from emailconfig import sendEmail

def createDir(directory):
    isdir = os.path.isdir(directory) 
    if not isdir:        
        try:
            os.makedirs(directory)
        except:
            print("Error with directory: "+directory)
            return False
    
    return True

def clearDir(directory):
    try:
        shutil.rmtree(directory)
        createDir(directory)
    except OSError as e:
        print("Error: %s: %s" % (directory, e.strerror))

def convertSto2Fasta(dirFile):
    posDot=dirFile.find('.')
    if (posDot>0):
        nameOnly=dirFile[:posDot]
        nameFastaFull=nameOnly+".fasta"
        records = SeqIO.parse(dirFile, "stockholm")
        count = SeqIO.write(records, nameFastaFull, "fasta")
        print("Converted %i records" % count)
    return nameFastaFull

def downloadFilesToLocal(filename, extension):
    #s3file/?code=prueba&ext=fasta&typed=1
    dataInput={
        "code":filename,
        "ext":extension,
        "typed":2
    }
    response = requests.get(URL_BACK_END_DEEPRESPRED+"s3file/", params=dataInput)
    rsp=response.json()
    if not rsp["error"]:
        print("File downloaded: "+rsp["fullNamePath"])
        return rsp["fullNamePath"]
    else:
        return ""


def sendEmailWithResults(idRequest, email):
    dataInput={
        "idRequest":idRequest
    }
    response = requests.get(URL_BACK_END_DEEPRESPRED+"resultsFilesxReq/", json=dataInput)
    print(response)
    rsp=response.json()
    fileList=rsp["files"]

    filesFull=[]
    for fileAux in fileList:
        nameFull=fileAux["nameFile"]
        print("Files results:")
        print(nameFull)
        pos=nameFull.find(".")
        name=nameFull[:pos]
        extension=nameFull[pos+1:]
        print(name)
        print(extension)
        fullPathDownloaded= downloadFilesToLocal(name, extension)
        if fullPathDownloaded!="":
            filesFull.append(fullPathDownloaded)


    #downloadedFiles
    sendEmail(email, filesFull, 2, idRequest)
    clearDir(FILES_DOWNLOADED)



def validateAndAssignResults(idRequest,pfamID,email):
    dataInput={
        "idRequest":idRequest,
        "pfamID":pfamID
    }
    response = requests.get(URL_BACK_END_DEEPRESPRED+"existsPFAMreq/", json=dataInput)
    rsp=response.json()

    existsPFAMresults=rsp["result"]

    if existsPFAMresults:
        #send email with results of prediction
        if(email!=""):
            sendEmailWithResults(idRequest, email)
        return True
    else:

        return False


def processingAlignments(dirPDBAux, dirResults):
    PDBAux_list = os.listdir(dirPDBAux)
    if len(PDBAux_list)>0:
        PDBAux_file=PDBAux_list[0]

        PDBAux_list = os.listdir(dirResults)



def verifyDirOrCreate(directory):
    isdir = os.path.isdir(directory) 
        
    if not isdir:        
        try:
            os.makedirs(directory)
        except:
            print("Error verifying or creating directory: "+directory)
            #sys.exit()