# %%
import wget
import requests
import os
import numpy as np
import pandas as pd
import sys
import re
import ssl

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

#this import is after because this file is in a subdirectory
from constants import ALGORITHM_PROCESSING
from constants import ALGORITHM_FOLDER

# %%
basePath=''
flagPFcode=True
pfam='PF18773'
param=''
filename=''
rangeSeq=5
PDBCodeStructure=[]
maxLongSeq=550
minLongSeq=15

# %%
if(len(sys.argv) > 1):    
    param=sys.argv[1]
    posDot=param.find('.')
    if(param=="default"):
        print("Default config")
    elif (posDot>0):
        extensionFile=param[posDot:]
        if(extensionFile==".txt"):
            print("Input file is a sequence. Exiting this family fragments process. Continuing prediction...")
            sys.exit()
            
        flagPFcode=False
        filename=param
    else:
        pfam=param

if(len(sys.argv) > 2): 
    param2=sys.argv[2]
    dirAux=os.path.join(param2, "target")
    isdir = os.path.isdir(dirAux) 
        
    if not isdir:        
        try:
            os.makedirs(dirAux)
        except:
            print("Error creating directory: "+dirAux)
            dirFileError=os.path.join(ALGORITHM_PROCESSING, "error.txt")
            text_file = open(dirFileError, "w")
            text_file.close()
            sys.exit()

    basePath=os.path.join(param2, "")


# %%
#quitar los cambios de linea en una secuencia
def preProcessText(data, initPoint, endPoint):
    print("Preprocessing complete sequence: min-"+str(initPoint)+" max-"+str(endPoint))

    seq=data
    pos=seq.find('\n')
    after=seq[pos+1:]
    after=after.replace('\n','')
    print("Initial longitude nr sequence: "+ str(len(after)))

    print("Position init of sequence: "+str(pos))
    print(after)
    
    #if((len(after)-2*rangeSeq)>=minLongSeq):
    if(((endPoint-initPoint)-2*rangeSeq)>=minLongSeq):
        print("reducing with min and max position from repeat fragments")
        initAux=initPoint+rangeSeq
        endAux=endPoint-rangeSeq+1
        print("cutting range ["+str(initAux)+", "+str(endAux)+"]")
        after=after[initAux:endAux]
        print(after)
    elif((endPoint-initPoint)>=minLongSeq):
        print("keeping longitude from min and max position from repeat fragments")
        print("cutting range ["+str(initPoint)+", "+str(endPoint)+"]")
        after=after[initPoint:endPoint]
        print(after)
    elif(  ((endPoint-initPoint)+2*rangeSeq)<=maxLongSeq  and (initPoint-rangeSeq>=pos+1) and (endPoint+rangeSeq-1<=len(after)) ):
        initAux=initPoint-rangeSeq
        endAux=endPoint+rangeSeq-1
        print("increasing with min and max position from repeat fragments")
        print("cutting range ["+str(initAux)+", "+str(endAux)+"]")
        after=after[initAux:endAux]
        print(after)
    
    print("Sequence length: "+str(len(after)))

    if((len(after)<=maxLongSeq) and (len(after)>=minLongSeq)):
        print("Sequence length ("+str(len(after))+") between range valid to prediction - ["+str(minLongSeq)+", "+str(maxLongSeq)+"]")
        before=seq[:pos+1]
        full=before+after
        return (True, full)
    
    print("Sequence length ("+str(endPoint-initPoint)+") not valid to prediction. Range valid - ["+str(minLongSeq)+", "+str(maxLongSeq)+"]")
    return (False, "")

# %%
#Generamos el archivo
def response2fasta (nameFile,response, initPoint, endPoint):
    print("Preprocessing "+ nameFile)
    rpta=preProcessText(response.text, initPoint, endPoint)
    
    if(rpta[0]):
        text_file = open(nameFile, "w")
        text_file.write(rpta[1])
        text_file.close()
        return True
    
    return False

# %%
def correctSeq(x):
    x=x.replace('.','')
    x=x.replace('-','')
    return x.upper()

# %%
#Generamos el archivo
def df2fastaIndividual (dfIn, type):
    if(type==1):
        preName=basePath+'target/is_'
    else:
        preName=basePath+'target/target_'

    #Organizamos la información tal cual la estructura inicial
    dfAux=pd.DataFrame()
    dfAux["agrupado"]=dfIn["encabezado"]+ os.linesep+ dfIn["secuencia"]+ os.linesep
   
    listContent = dfAux['agrupado'].tolist()
    listName = dfIn['id'].tolist()
    
    for i in range(len(listName)):
        nameFile=preName+listName[i]+'_'+str(i)+'.fasta' #is: seq independient
        print("Generating file: "+ nameFile)
        text_file = open(nameFile, "w")
        text_file.write(listContent[i])
        text_file.close()
print("Generating Fasta files: completed sequences and only fragments..............")
# %%
#Generamos el FASTA desde Pfam
if flagPFcode:
    try:
        #urlFasta='https://pfam.xfam.org/family/alignment/download/format?acc='+pfam+'&alnType=full&format=fasta&order=t&case=l&gaps=default&download=1'
        urlFasta='https://pfam.xfam.org/family/alignment/download/format?acc='+pfam+'&alnType=seed&format=fasta&order=t&case=l&gaps=default&download=1'
        print(urlFasta)
        ssl._create_default_https_context = ssl._create_unverified_context
        filename = wget.download(urlFasta, out=ALGORITHM_PROCESSING)
        print("File Fasta downloaded:")
        print(filename)
    except:
        print("Fail downloading Fasta")
        dirFileError=os.path.join(ALGORITHM_PROCESSING, "error.txt")
        text_file = open(dirFileError, "w")
        text_file.close()
        sys.exit()
else:
    filename=param

# %%
#filename='PF00806_full.txt'
filename

# %%
#df_DP_TR = pd.read_csv('SP_TR.txt', sep=" ",header=None)
df_DP_TR = pd.read_csv(ALGORITHM_FOLDER+'/SP_collection.txt', sep=" ",header=None)
df_DP_TR.rename({0: 'uniprotAccession', 1: 'uniprotId'}, axis=1, inplace=True)
df_DP_TR.head()

# %%
file1 = open(filename, 'r')
linesDocInput = file1.readlines()
 
tipoDoc=1 #1:Fasta 2:Stocolmo
seqIds=[]
count = 0
encabezados=[]
ids=[]
secuencias=[]
flagSeq=True
lineSeq=''

for line in linesDocInput:
    count += 1

    if (count==1):
        posTipoDoc=line.find('#')
        if posTipoDoc>=0:
            tipoDoc=2
            print("Input in Stockholm format")
        else:
            print("Input in Fasta format")
    
    if tipoDoc==1:
        posHeaderFlag=line.find('>')
        if (posHeaderFlag>=0): #Es encabezado
            if count==1:
                flagSeq=False
            else:
                flagSeq=True
            fin=line.find('/')
            sub=(line.strip())[1:fin]        

            encabezados.append(line.strip())
            ids.append(sub.strip())
        else:
            if flagSeq:
                secuencias.append(lineSeq.strip())
                lineSeq=''
                flagSeq=False                
            lineSeq=lineSeq+line.strip() #concatena las secuencias encontradas
            

file1.close()

# %%
dfGeneral = pd.DataFrame(list(zip(encabezados, ids, secuencias)),
               columns =['encabezado', 'id', 'secuencia'])
dfGeneral.head()
dfGeneral.shape

# %%
#Convertir a DF
dfAccessions = pd.DataFrame(ids, columns =['ids2search'])
dfAccessions=dfAccessions.drop_duplicates()
print("N° items:",dfAccessions.shape)
dfAccessions.head()

# %%
#Obtener los uniprot accessions a partir de los IDs
merged_inner = pd.merge(left=df_DP_TR, right=dfAccessions, left_on='uniprotId', right_on='ids2search')
merged_inner

# %%
#lo convertimos a lista
accessions2search = merged_inner['uniprotAccession'].tolist()
accessions2search

# %%
def obtenerInfoEstructura(rsp):
    #Obtenemos la entrada de Uniprot para poder linkearlo a su PDB
    uniprot_acc=""
    interpro_name=""
    pfam=""
    pdb_accession=""
    uniprot_id=""

    uniprot_id=rsp["responseHeader"]["params"]["q"]
    numPDBFound=rsp["response"]["numFound"]
    print(uniprot_id)

    if(numPDBFound!=0):
        uniprot_acc=rsp["response"]["docs"][0]["entry_uniprot_accession"][0]
        #interpro_name=rsp["response"]["docs"][0]["interpro_repeat_name"][0]
        #pfam=rsp["response"]["docs"][0]["pfam"][0]
        pdb_accession=rsp["response"]["docs"][0]["pdb_accession"]

        print("Uniprot accession: ", uniprot_acc)
        print("Interpro Name: ", interpro_name)
        print("Num. PDB found: ", numPDBFound)
        print("PDB accession: ", pdb_accession)
        print("PFAM: ", pfam)
        print("---------")

        PDBCodeStructure.append(pdb_accession)
        
        return True
    else:
        print("--")
        print("No se obtuvieron más datos")
        print("---------")
    
    return False

# %%
#dat='BAT1_PARRH'
#dat='BAT1_MYCRK'
#seq=['BAT1_MYCRK','BAT1_PARRH']

conEstructura=[]
for dat in accessions2search:
    url='https://www.ebi.ac.uk/pdbe/search/pdb/select?q=uniprot_accession:'+dat+'&wt=json'
    response = requests.get(url, data=[])
    rsp=response.json()
    #rsp
    if (obtenerInfoEstructura(rsp)):
        conEstructura.append(dat)
        
print("Tienen estructura: ", conEstructura)

# %%
#Convertir a DF
df_conEstructura = pd.DataFrame(conEstructura, columns =['accessionsEstructura'])
df_conEstructura.shape

# %%
#Obtener los uniprot ID a partir de los accessions
merged_inner2 = pd.merge(left=df_DP_TR, right=df_conEstructura, left_on='uniprotAccession', right_on='accessionsEstructura')
merged_inner2.shape

# %%
dfGeneral.head()

# %%
#Obtenemos los datos de encabezados y secuencia de los que tienen estructura
#dfConEstructuras = dfGeneral[dfGeneral.id.isin(merged_inner2['uniprotId'])]
#dfConEstructuras.shape

# %%
#Obtenemos los datos de encabezados y secuencia de los que tienen estructura
dfSinEstructuras = dfGeneral[~dfGeneral.id.isin(merged_inner2['uniprotId'])]
dfSinEstructuras.shape

# %%
#Organizamos la información tal cual la estructura inicial
#dfAux=pd.DataFrame()
#dfAux["agrupado"]=dfConEstructuras["encabezado"]+ os.linesep+dfConEstructuras["secuencia"]
#dfAux.head()
#dfConEstructuras2=dfConEstructuras.copy()
#dfConEstructuras2['secuencia'] = dfConEstructuras2['secuencia'].apply(correctSeq)
#dfConEstructuras2.shape

# %%
#generar archivos
#df2fastaIndividual(dfConEstructuras2, 2)

# %%
#Generamos el archivo
#print(pfam)
#nombre=pfam
#if (dfAux.size!=0):
    #np.savetxt('target/'+nombre+'_target.fasta', dfAux.values, fmt='%s')
#else:
    #print("No se obtuvo ninguna secuencia que tenga estructura en PDB")

# %%
#=====================================================================================
#=====================================================================================

# %%
#PROCESAMOS LAS SECUENCIAS QUE NO TIENEN ESTRUCTURAS

#Alternativa 1 (nr): Eliminacion o union de repetidas con mejor inicio y fin-> se saca el uniprot_accession, se buscan en archivos el uniprot_id y se busca la secuencia completa
#Alternativa 2 (is): Un archivo fasta por cada secuencia (check)

# %%
#Alternativa1:
dfSinEstructuras1=dfSinEstructuras.copy()
dfSinEstructuras1.shape
dfSinEstructuras1.head()

# %%
def getIniIndexSeq(x):
    pos1=x.find('/')
    pos2=x.find('-')
    return x[pos1+1:pos2]

# %%
def getEndIndexSeq(x):
    pos1=x.find('-')
    pos2=len(x)
    return x[pos1+1:pos2]

# %%
dfSinEstructuras1['iniIndex'] = dfSinEstructuras1['encabezado']. apply(getIniIndexSeq)
dfSinEstructuras1['endIndex'] = dfSinEstructuras1['encabezado']. apply(getEndIndexSeq)
dfSinEstructuras1.head()
dfSinEstructuras1.shape

# %%
merged_innerAux=pd.DataFrame(dfSinEstructuras1, columns =['id','iniIndex','endIndex'])
merged_innerAux['iniIndex'] = pd.to_numeric(merged_innerAux['iniIndex'])
merged_innerAux['endIndex'] = pd.to_numeric(merged_innerAux['endIndex'])
merged_innerAux.dtypes
merged_innerAux.shape
merged_innerAux.head()

# %%
auxMin=merged_innerAux.groupby(['id']).min()
auxMin=pd.DataFrame(auxMin, columns =['iniIndex'])
auxMin.reset_index(level=0, inplace=True)
auxMin.shape
auxMin.head()

# %%
auxMax=merged_innerAux.groupby(['id']).max()
auxMax=pd.DataFrame(auxMax, columns =['endIndex'])
auxMax.reset_index(level=0, inplace=True)
auxMax.shape

# %%
merged_inner4 = pd.merge(left=auxMin, right=auxMax, left_on='id', right_on='id')
merged_inner4.head()
#merged_inner4.shape

# %%
#prueba=merged_inner4.copy()
#prueba["resta"]=prueba["endIndex"]-prueba["iniIndex"]
#prueba.head()
#prueba["resta2"]=prueba["resta"]>500
#prueba[prueba["resta"]>500]

# %%
#lo convertimos a lista
id_seqs = merged_inner4['id'].tolist()
iniIndexSeq = merged_inner4['iniIndex'].tolist()
endIndexSeq = merged_inner4['endIndex'].tolist()
id_seqs[0]

# %%
counter=0
nSequence=0
for item in id_seqs:
    url='https://www.uniprot.org/uniprot/'+item+'.fasta'
    rspta = requests.get(url, data=[])
    #print(rspta.text)
    if (len(rspta.text)!=0):
        rptaFile=response2fasta(basePath+'target/nr_'+item+'_'+str(counter)+'.fasta', rspta, iniIndexSeq[nSequence], endIndexSeq[nSequence])  #nr: no repeat
        if rptaFile:
            counter += 1
    nSequence += 1

# %%
#==================================================================================================

# %%
#Alternativa2:
dfSinEstructuras2=dfSinEstructuras.copy()
dfSinEstructuras2.shape

# %%
dfSinEstructuras2['secuencia'] = dfSinEstructuras2['secuencia']. apply(correctSeq)
dfSinEstructuras2

# %%
#generar archivos
df2fastaIndividual(dfSinEstructuras2, 1) 
os.remove(filename)
# %%
#Descargando PDB de la secuencia con los fragmentos con estructura
if len(PDBCodeStructure)>0:
    dirAux=os.path.join(basePath, "auxFiles")
    isdir = os.path.isdir(dirAux) 
        
    if not isdir:        
        try:
            os.makedirs(dirAux)
        except:
            print("Error creating directory: "+dirAux)
            dirFileError=os.path.join(ALGORITHM_PROCESSING, "error.txt")
            text_file = open(dirFileError, "w")
            text_file.close()
            sys.exit()

    try:
        urlFasta='https://files.rcsb.org/download/'+PDBCodeStructure[0]+'.pdb'
        filenamePDB = wget.download(urlFasta, out=dirAux)
        print("File PDB with estructure of repeat protein with fragments of the studied family:")
        print(filenamePDB)
        print("---------------------------------")
        print(" ")
    except:
        print("Fail downloading PDB")