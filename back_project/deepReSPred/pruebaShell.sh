#!/bin/bash

echo "---------------------------Start------------------------------"


# Set this to point to the DMPfold directory
dmpfolddir=/home/spalomino/R1.2_verificacion_func/dmpfold/DMPfold
#dmpfolddir=/home/layla/dmpfold/DMPfold #enGuerrera


if [ "$#" -lt 1 ]; then
    echo "Usage: run_dmpfold.sh (PFAMCODE|filename.fasta) [outputDir]"
    exit 1
fi

pfamCode=$1
echo "Prediction preprocessing of" $pfamCode

dirAux="$( pwd )"
if [ "$#" -gt 1 ]; then
    #/home/spalomino/datosRepeatPrueba/pruebaDir
    dirAux=$2
fi

dirFlags=$dirAux/flagsEnding

echo "Results directory: " $dirAux
echo ""

if [ -e $dirFlags ]; then
    echo "Directory $dirFlags already exists."
#    exit 1
else #esto no estaba
    echo "Creating directory $dirFlags"
    mkdir $dirFlags
fi

echo $dirAux > $dirFlags/flags.txt