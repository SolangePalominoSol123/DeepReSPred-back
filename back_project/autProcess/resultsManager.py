from sys import maxsize
from werkzeug.utils import secure_filename
from auxiliarFunctionsDaemon import clearDir
import requests
import fnmatch
import subprocess
import os
import shutil
import sys
import re

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from constants import URL_BACK_END_DEEPRESPRED
from constants import S3_UPLOAD_DIR

def processingResults(dirPDBAux, dirResults, idRequest):
    PDBAux_list = os.listdir(dirPDBAux)

    flagPDBAux=False
    if len(PDBAux_list)>0:
        print("There is a PDB aux to evaluate predicted fragments...")
        PDBAux_file=PDBAux_list[0]
        PDBAux_fileFull=os.path.join(dirPDBAux, secure_filename(PDBAux_file))
        print(PDBAux_fileFull)
        flagPDBAux=True
    else:
        print("There is not any PDB aux to evaluate predicted fragments...")
        

    group=1
    dirResults_list = os.listdir(dirResults)
    for dirResult in dirResults_list:
        dirResult_full=os.path.join(dirResults, secure_filename(dirResult)) #dir ../results/test_seq*/
        print("\n------------------------------------------------------")
        print("Current dir: "+dirResult_full)
        print("Subgroup: "+str(group))

        #Final
        fileFullInput=""
        fileFullPDB=""
        fileFull21c=""
        fileFullmap=""
        fileFullAlign=""
        isFragmentFlag=False


        #Auxiliar
        dirFilesResult=os.path.join(dirResult_full, secure_filename("output"))
        listFilesInputIS=fnmatch.filter(os.listdir(dirResult_full), 'is_*.fasta')
        listFilesInputNR=fnmatch.filter(os.listdir(dirResult_full), 'nr_*.fasta')
        listFiles21c=fnmatch.filter(os.listdir(dirResult_full), '*.21c')
        listFilesMap=fnmatch.filter(os.listdir(dirResult_full), '*.map')

        maxGen=0
        #Is a fragment, not a complete sequence
        if len(listFilesInputIS)>0: 
            print("\nEvaluating a fragment...")
            listFilesResults=fnmatch.filter(os.listdir(dirFilesResult), 'final_*.pdb')

            if flagPDBAux:
                maxGen=0
                fileResultFullGen=""
                for fileResult in listFilesResults:
                    print("Evaluating TM-align between:")
                    #TMalign
                    fileResultFull=os.path.join(dirFilesResult, secure_filename(fileResult)) #.PDB generated                    
                    print(fileResultFull)
                    print(PDBAux_fileFull)

                    proc = subprocess.Popen(['TMalign', PDBAux_fileFull, fileResultFull], stdout=subprocess.PIPE)
                    output = str(proc.stdout.read())

                    maxTM=0
                    for m in re.finditer('TM-score= ', output):
                        posValue=m.end()
                        value=float(output[posValue:posValue+7])
                        print("TM-score: "+str(value))
                        #value=0.6 ######################################################################
                        if value>maxTM:
                            maxTM=value

                    print("TM-score_aux: "+str(maxTM))

                    if maxTM>maxGen:
                        maxGen=maxTM
                        fileResultFullGen=fileResultFull


                if maxGen>0.5:
                    #aprobado fileResultFullGen .pdb
                    print("Fragment aproved...")
                    fullFragmentInput=os.path.join(dirResult_full, secure_filename(listFilesInputIS[0])) #.fasta
                    fileFullInput=fullFragmentInput
                    fileFullPDB=fileResultFullGen
                    print(fullFragmentInput)
                    print(fileResultFullGen)
                    isFragmentFlag=True

                    fullPathAlign1=os.path.join(dirResult_full, secure_filename("TM.sup"))
                    fullPathAlign2=os.path.join(dirResult_full, secure_filename("TM.sup_atm"))
                    proc = subprocess.Popen(['TMalign', fileFullPDB, PDBAux_fileFull, "-o", fullPathAlign1])
                    fileFullAlign=fullPathAlign2
                    print("TM-align file generated: "+fileFullAlign)
                    
            else:
                #no hay PDB aux
                if(len(listFilesResults)>0):
                    print("There is not PDB aux to evaluate TM-score. Selecting the first: final_1.pdb")
                    #fileResultFull=os.path.join(dirFilesResult, secure_filename(listFilesResults[0])) #.PDB generated  
                    fileResultFull=os.path.join(dirFilesResult, secure_filename("final_1.pdb")) #.PDB generated  
                    fullFragmentInput=os.path.join(dirResult_full, secure_filename(listFilesInputIS[0])) #.fasta
                    isFragmentFlag=True
                    fileFullInput=fullFragmentInput
                    fileFullPDB=fileResultFull
                else:
                    print("There is not PDB aux to evaluate TM-score, nor any predicted structure PDB")


        #Is a complete sequence
        if len(listFilesInputNR)>0: 
            print("\nEvaluating a complete sequence...")
            listFilesResults=fnmatch.filter(os.listdir(dirFilesResult), 'final_1.pdb')

            if len(listFilesResults)>0:
                fileResultFull=os.path.join(dirFilesResult, secure_filename(listFilesResults[0])) #.PDB generated
                fullFragmentInput=os.path.join(dirResult_full, secure_filename(listFilesInputNR[0])) #.fasta
                
                print("NR - Complete sequence:")
                print(fileResultFull)
                print(fullFragmentInput)
                fileFullInput=fullFragmentInput
                fileFullPDB=fileResultFull
                isFragmentFlag=False
            else:
                print("Any predicted structure PDB was finded")
                


        fileFull21c=os.path.join(dirResult_full, secure_filename(listFiles21c[0])) #.21c
        fileFullmap=os.path.join(dirResult_full, secure_filename(listFilesMap[0])) #.map

        if(fileFullInput!="" and fileFullPDB!="" and fileFull21c!="" and fileFullmap!=""):
            print("----------")
            print("Good prediction")
            print(fileFullInput)
            print(fileFullPDB)
            print(fileFull21c)
            print(fileFullmap)
            print("Is Fragment: "+str(isFragmentFlag))
            print("Subgroup: " + str(group))
            print("ID Request: "+str(idRequest))
            print("----------")

            print("\nSaving data to DB and S3 bucket...")
            #Fasta
            posDot=fileFullInput.find(".")
            dataInput={
                "idRequest" : idRequest,
                "idSubGroup" : group,
                "haveStructure" : flagPDBAux,
                "extension" : fileFullInput[posDot:],
                "isFragment" : isFragmentFlag,
                "dbAlgorithm" : "PFAM",
                "tmscore" : 0,
                "isResult" : False
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"filexreqInfo/", json=dataInput)
            print(response)
            rsp=response.json()
            registeredFasta=rsp["nameFile"]

            regFullAfter=os.path.join(S3_UPLOAD_DIR, secure_filename(registeredFasta))

            shutil.copy(fileFullInput, regFullAfter)
            posDot=registeredFasta.find(".")
            #Upload to S3
            dataInput={
                "name" : registeredFasta[:posDot],
                "extension" : registeredFasta[posDot:]
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"s3file/", json=dataInput)

            #---------------

            #PDB
            posDot=fileFullPDB.find(".")
            dataInput={
                "idRequest" : idRequest,
                "idSubGroup" : group,
                "haveStructure" : flagPDBAux,
                "extension" : fileFullPDB[posDot:],
                "isFragment" : isFragmentFlag,
                "dbAlgorithm" : "PFAM",
                "tmscore" : maxGen,
                "isResult" : True
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"filexreqInfo/", json=dataInput)
            print(response)
            rsp=response.json()
            registeredPDB=rsp["nameFile"]

            regFullAfter=os.path.join(S3_UPLOAD_DIR, secure_filename(registeredPDB))

            shutil.copy(fileFullPDB, regFullAfter)
            posDot=registeredPDB.find(".")
            #Upload to S3
            dataInput={
                    "name" : registeredPDB[:posDot],
                    "extension" : registeredPDB[posDot:]
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"s3file/", json=dataInput)

            #-------------------------------

            #21c
            posDot=fileFull21c.find(".")
            dataInput={
                "idRequest" : idRequest,
                "idSubGroup" : group,
                "haveStructure" : flagPDBAux,
                "extension" : fileFull21c[posDot:],
                "isFragment" : isFragmentFlag,
                "dbAlgorithm" : "PFAM",
                "tmscore" : 0,
                "isResult" : False
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"filexreqInfo/", json=dataInput)
            print(response)
            rsp=response.json()
            registered21c=rsp["nameFile"]

            regFullAfter=os.path.join(S3_UPLOAD_DIR, secure_filename(registered21c))

            shutil.copy(fileFull21c, regFullAfter)
            posDot=registered21c.find(".")
            #Upload to S3
            dataInput={
                    "name" : registered21c[:posDot],
                    "extension" : registered21c[posDot:]
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"s3file/", json=dataInput)

            #--------------

            #map
            posDot=fileFullmap.find(".")
            dataInput={
                "idRequest" : idRequest,
                "idSubGroup" : group,
                "haveStructure" : flagPDBAux,
                "extension" : fileFullmap[posDot:],
                "isFragment" : isFragmentFlag,
                "dbAlgorithm" : "PFAM",
                "tmscore" : 0,
                "isResult" : False
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"filexreqInfo/", json=dataInput)
            print(response)
            rsp=response.json()
            registeredMap=rsp["nameFile"]

            regFullAfter=os.path.join(S3_UPLOAD_DIR, secure_filename(registeredMap))

            shutil.copy(fileFullmap, regFullAfter)
            posDot=registeredMap.find(".")
            #Upload to S3
            dataInput={
                    "name" : registeredMap[:posDot],
                    "extension" : registeredMap[posDot:]
            }
            response = requests.post(URL_BACK_END_DEEPRESPRED+"s3file/", json=dataInput)

            #---------------

            #TMalign
            if (flagPDBAux and fileFullAlign!=""):
                posDot=fileFullAlign.find(".")
                dataInput={
                    "idRequest" : idRequest,
                    "idSubGroup" : group,
                    "haveStructure" : flagPDBAux,
                    "extension" : fileFullAlign[posDot:],
                    "isFragment" : True,
                    "dbAlgorithm" : "PFAM",
                    "tmscore" : maxGen,
                    "isResult" : True
                }
                response = requests.post(URL_BACK_END_DEEPRESPRED+"filexreqInfo/", json=dataInput)
                print(response)
                rsp=response.json()
                registeredAlign=rsp["nameFile"]

                regFullAfter=os.path.join(S3_UPLOAD_DIR, secure_filename(registeredAlign))

                shutil.copy(fileFullAlign, regFullAfter)
                posDot=registeredAlign.find(".")
                #Upload to S3
                dataInput={
                        "name" : registeredAlign[:posDot],
                        "extension" : registeredAlign[posDot:]
                }
                response = requests.post(URL_BACK_END_DEEPRESPRED+"s3file/", json=dataInput)
            



        group+=1

    ############################################ CLEAR ALL
    clearDir(dirPDBAux)
    clearDir(dirResults)
    clearDir(S3_UPLOAD_DIR)


"""
dirpath="/home/spalomino/DeepReSPred-back/back_project/autProcess/processingPred/target"
dirpath2="/home/spalomino/DeepReSPred-back/back_project/autProcess/processingPred/results"
dirpath3="/home/spalomino/DeepReSPred-back/back_project/autProcess/processingPred/auxFiles"
dirpath4="/home/spalomino/DeepReSPred-back/back_project/autProcess/processingPred/flagsEnding"

canti=len(fnmatch.filter(os.listdir(dirpath), '*.fasta')) #cantidad de inputs
canti2=len(fnmatch.filter(os.listdir(dirpath2), 'test_*')) #cantidad de archivos intermedios generados
canti3=len(fnmatch.filter(os.listdir(dirpath3), '*pdb')) #cantidad de archivos intermedios generados
canti4=len(fnmatch.filter(os.listdir(dirpath4), '*_txt')) #cantidad de flags (procesos terminados)

print(canti)
print(canti2)
print(canti3)
print(canti4)

processingResults(dirpath3, dirpath2,"AAAAAAA")
"""