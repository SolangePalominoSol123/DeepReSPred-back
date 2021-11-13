# %%
import os
import numpy as np
import pandas as pd

# %%
filenameTR='uniprot_trembl.fasta'
#filenameTR='uniprot_sprot_v2.fasta'
filenameSP='uniprot_sprot.fasta'

# %%
uniprotIds=[]
uniprotAccessions=[]

#Abrimos el archivo de TremblProt

fileTR = open(filenameTR, 'r')
linesTR = fileTR.readlines()

countTR=0
for line in linesTR:
    line=line.strip()
    inicio=line.find('>')
    
    if (inicio>-1): #Es encabezado
        countTR += 1
        flag1=line.find('|')
        flag2=line.find('|',flag1+1)
        flag3=line.find(' ',flag2+1)

        accession_uni=(line.strip())[flag1+1:flag2]
        id_uni=(line.strip())[flag2+1:flag3]

        uniprotAccessions.append(accession_uni)
        uniprotIds.append(id_uni)    

fileTR.close()

#Abrimos el archivo de SwissProt
        
fileSP = open(filenameSP, 'r')
linesSP = fileSP.readlines()

countSP = 0
for line in linesSP:
    line=line.strip()
    inicio=line.find('>')

    if (inicio>-1): #Es encabezado
        countSP += 1
        flag1=line.find('|')
        flag2=line.find('|',flag1+1)
        flag3=line.find(' ',flag2+1)

        accession_uni=(line.strip())[flag1+1:flag2]
        id_uni=(line.strip())[flag2+1:flag3]

        uniprotAccessions.append(accession_uni)
        uniprotIds.append(id_uni)   

dfGeneral = pd.DataFrame(list(zip(uniprotAccessions, uniprotIds)),
               columns =['uniprotAccession', 'uniprotId'])

fileSP.close()

print(countTR,countSP)

# %%
dfGeneral = dfGeneral.drop_duplicates()
dfGeneral

# %%
np.savetxt(r'SP_collection.txt', dfGeneral.values, fmt='%s')

# %%
