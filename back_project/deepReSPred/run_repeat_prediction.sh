#!/bin/bash

echo "---------------------------Start------------------------------"


# Set this to point to the DMPfold directory
dmpfolddir=/home/ladmin/algPrograms/DMPfold
mappingFastaDir=/home/ladmin/DeepReSPred-back/back_project/deepReSPred



if [ "$#" -lt 1 ]; then
    echo "Usage: run_dmpfold.sh (PFAMCODE|filename.fasta) [outputDir]"
    exit 1
fi

pfamCode=$1
echo "Prediction preprocessing of" $pfamCode


dirAux="$( pwd )"
if [ "$#" -gt 1 ]; then
    dirAux=$2
fi

dirFlags=$dirAux/flagsEnding

echo "Results directory: " $dirAux
echo ""

#COMENZAMOS A MEDIR EL TIEMPO
inicio_ns_General=`date +%s%N`
inicio_General=`date +%s`
echo "Started in (ns):" $inicio_ns_General

#Generar todos los archivos segun las modificaciones planteadas
#Todos los archivos se generarán dentro de $dirAux/target p.j. python3 MappingFasta.py default target4/
python3 $mappingFastaDir/MappingFasta.py $pfamCode $dirAux
#python3 MappingFasta.py default $dirAux #thiss-----------------

echo ""
echo "---------------GENERATING INTERMEDIATE FILES---------------"
echo ""

counter=0

#recorremos los archivos ***.fasta para generar archivos intermedios .map y .21c

for file in $dirAux/target/*.fasta; do 
        mkdir -p $dirAux/results/test_seq$counter
        nameExtFileIs=$(basename $file)
        cp $file $dirAux/results/test_seq$counter
        cd $dirAux/results/test_seq$counter
        echo "--- generating intermediate files target File:"$nameExtFileIs
        csh $dmpfolddir/seq2maps.csh $file
        counter=$((counter+1))
done

echo ""
echo ""

#:''
echo ""
echo "---------------EXECUTING DMPFOLD ALGORITHM---------------"
echo ""


nTests=0

for directory in $dirAux/results/test*; do
    echo "----Prediction n°" $nTests
	rm $directory/*.temp.fasta
    find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
    echo $directory/*.fasta
    sh $dmpfolddir/run_dmpfold.sh $directory/*.fasta $directory/*.21c $directory/*.map $directory/output $dirFlags

    nTests=$((nTests+1)) 
done


echo ""
echo ""
echo "-------------------End------------------"
echo "N° Tests:" $nTests

#TERMINAMOS DE MEDIR EL TIEMPO
fin_ns_General=`date +%s%N`
fin_General=`date +%s`
echo "End of general predictions in (ns):" $fin_ns_General


total_ns_General=$(($fin_ns_General-$inicio_ns_General))
total_General=$(($fin_General-$inicio_General))
echo "It has last: -$total_ns_General- nanoseconds, -$total_General- seconds"