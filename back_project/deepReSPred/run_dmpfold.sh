#!/bin/bash

# DMPfold
# Iteratively generate models using CNS and deep neural nets to
#  generate updated constraints
# Arguments are FASTA file, 21c file, map file, out directory,
#  number of cycles (optional) and models per cycle (optional)

# Original script by David T. Jones, June 2018

# Copyright (C) 2018 University College London

# License: GPLv3

# Set this to point to the DMPfold directory
dmpfolddir=/home/ladmin/algPrograms/DMPfold

# Set this to point to the CNS setup script
STOREPATH=$PATH
. /home/ladmin/algPrograms/cns_solve_1.3/cns_solve_env.sh
export PATH="$STOREPATH:$PATH" # CNS setup can remove some things from the path

bindir=$dmpfolddir/bin
cnsdir=$dmpfolddir/cnsfiles
export CNS_CUSTOMMODULE=$cnsdir

# Number of cycles
ncycles=3

# Number of models per cycle
nmodels=50

perc1=0.42
perc2=0.43
hbrange=4
hbprob1=0.85
hbprob2=0.85

if [ "$#" -lt 2 ]; then
    echo "Usage: run_dmpfold.sh target.fasta target.21c target.map outdir endFlagdir [ncycles nmodels-per-cycle]"
    exit 1
fi

DIR="$( cd "$( dirname "$1" )" && pwd )"
target=$(basename "${1%.*}")
targseq=$DIR/$(basename $1)
DIR="$( cd "$( dirname "$2" )" && pwd )"
targ21c=$DIR/$(basename $2)
DIR="$( cd "$( dirname "$3" )" && pwd )"
targmap=$DIR/$(basename $3)

outdir=$4
endFlagdir=$5


if [ "$#" -gt 6 ]; then
    ncycles=$6
    nmodels=$7
fi

if [ "$#" -gt 8 ]; then
    perc1=$8
    perc2=$9
fi

if [ -e $outdir ]; then
    echo "Directory $outdir already exists."
#    exit 1
else #esto no estaba
    echo "Creating directory $outdir."
    mkdir $outdir
fi

if [ -e $endFlagdir ]; then
    echo "Directory $endFlagdir already exists."
#    exit 1
else #esto no estaba
    echo "Creating directory $endFlagdir."
    mkdir $endFlagdir
fi

#mkdir $outdir

cd $outdir
#rm * #esto no estaba

#COMENZAMOS A MEDIR EL TIEMPO
inicio_ns=`date +%s%N`
inicio=`date +%s`

$bindir/fasta2tlc < $targseq > input.seq
$bindir/fasta2tlc < $targseq > input.seq

cns < $cnsdir/gseq.inp > gseq.log
if [ $? -ne 0 ]; then
    echo $?
    echo "CNS execution failed!"
    find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
    echo "CNS execution failed1" > $endFlagdir/err_$target.txt
    exit 1
fi
cns < $cnsdir/extn.inp > extn.log
if [ $? -ne 0 ]; then
    echo "CNS execution failed!"
    find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
    echo "CNS execution failed2" > $endFlagdir/err_$target.txt
    exit 1
fi

python3 $dmpfolddir/nn/dmp-softmax/pytorch_dmp_distpred.py $targ21c $targmap > rawdistpred.current

cat rawdistpred.current | perl $bindir/dist2dualbound.pl $perc1 > contacts.current

if [ $? -ne 0 ]; then
    echo "Distance prediction failed!"
    find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
    echo "Distance prediction failed!" > $endFlagdir/err_$target.txt
    exit 1
fi

python3 $dmpfolddir/nn/dmp-hb/pytorch_dmp_hbpred.py $targ21c $targmap | sort -g -r -k 5 | perl $bindir/listcontacts.pl $hbrange $hbprob1 > hbcontacts.current

if [ $? -ne 0 ]; then
    echo "Hydrogen bond prediction failed!"
    find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
    echo "Hydrogen bond prediction failed!" > $endFlagdir/err_$target.txt
    exit 1
fi

python3 $dmpfolddir/nn/torpred/pytorch_torcov_pred.py $targ21c $targmap > dihedral.tbl

if [ $? -ne 0 ]; then
    echo "Torsion angle prediction failed!"
    find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
    echo "Torsion angle prediction failed!" > $endFlagdir/err_$target.txt
    exit 1
fi

ln -s $dmpfolddir/modcheck/dope.scr .
ln -s $dmpfolddir/modcheck/modcheckpot.dat .
ln -s $bindir/qmodcheck .
ln -s $bindir/qmodope_mainens .

counter=1
until [ $counter -gt $ncycles ]; do
	echo "iteracion " $counter " de " $ncycles
    if [ $counter -gt 1 ]; then #no se ejecuta esto en la primera iteracion
        \mv contacts.current contacts.$((counter - 1))
        \mv rawdistpred.current rawdistpred.$((counter - 1))
        \mv hbcontacts.current hbcontacts.$((counter - 1))

        python3 $dmpfolddir/nn/dmp-softmax/pytorch_dmp_iterdistpred_cb.py $targ21c $targmap best_qdope.pdb > rawdistpred.current

        cat rawdistpred.current | perl $bindir/dist2dualbound.pl $perc2 > contacts.current

        if [ $? -ne 0 ]; then
            echo "Iterated distance prediction failed!"
            find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
            echo "Iterated distance prediction failed!" > $endFlagdir/err_$target.txt
            exit 1
        fi

        python3 $dmpfolddir/nn/dmp-hb/pytorch_iterdmp_hbpred.py $targ21c $targmap best_qdope.pdb | sort -g -r -k 5 | perl $bindir/problistcontacts.pl $hbrange $hbprob2 > hbcontacts.current

        if [ $? -ne 0 ]; then
            echo "Iterated hydrogen bond prediction failed!"
            find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
            echo "Iterated hydrogen bond prediction failed!" > $endFlagdir/err_$target.txt
            exit 1
        fi
    fi
	#esto se ejecuta para todas las iteraciones
    if [ ! -s dihedral.tbl ]; then #verfica si esta vacio
        echo "No valid torsion angles."
        find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
        echo "No valid torsion angles." > $endFlagdir/err_$target.txt
        exit 1
    fi
 
    if [ ! -s contacts.current ]; then
        echo "No valid current contacts."
        find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
        echo "No valid current contacts." > $endFlagdir/err_$target.txt
        exit 1
    fi

    if [ ! -s hbcontacts.current ]; then
        echo "No valid current hydrogen bonds."
        find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
        echo "No valid current hydrogen bonds." > $endFlagdir/err_$target.txt
        exit 1
    fi
	
    $bindir/contact2noe $targseq contacts.current > contact.tbl 
    $bindir/hbond2noe hbcontacts.current > hbond.tbl
    $bindir/hbond2ssnoe hbcontacts.current > ssnoe.tbl

    \rm -f $target*.pdb*

	RANDOM=$$ #le agregue esto
    seed=$RANDOM
    echo "seed = " $seed
    sed "s/_TARGET_NAME_/$target/" $cnsdir/dgsa.inp | sed "s/_SEED_/$seed/" | sed "s/_NMODELS_/$nmodels/g" > dgsa.inp 
    cns < dgsa.inp > dgsa.log
	echo "revisar dgsa.log"

    if [ $? -ne 0 ]; then
        echo "CNS execution failed!"
        find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
        echo "CNS execution failed!" > $endFlagdir/err_$target.txt
        exit 1
    fi
    lc=$(grep "NOE-ERR: allocation for NOE-restraints exceeded" dgsa.log | wc -l)
    if [ $lc -gt 0 ]; then
        echo "Looks like you need to increase nrestraints in cns_solve_1.3/modules/nmr/readdata to a higher number to deal with this length of sequence."
        find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
        echo "Looks like you need to increase nrestraints in cns_solve" > $endFlagdir/err_$target.txt
        exit 1
    fi
    lc=$(grep "CSTRAN-ERR: allocation for assignments exceeded" dgsa.log | wc -l)
    if [ $lc -gt 0 ]; then
        echo "Looks like you need to increase nassign in cns_solve_1.3/modules/nmr/readdata to a higher number to deal with this length of sequence."
        find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete
        echo "Looks like you need to increase nassign in cns_solve_1.3" > $endFlagdir/err_$target.txt
        exit 1
    fi

	dirAux="$( pwd )"
	echo "current directory: " $dirAux
    for file in ${target}_[1-9]*.pdb; do
        $bindir/pdbhfilt < $file | perl $bindir/pdborder.pl | grep ATOM >> ensemble.$counter.pdb
        echo END >> ensemble.$counter.pdb
    done

    $bindir/tmclust ensemble.$counter.pdb

    if [ -s clustreps.pdb ]; then
        ./qmodope_mainens CLUSTER_001.pdb
    else
        ./qmodope_mainens ensemble.$counter.pdb
    fi

	counter=$((counter+1))
done

cat ensemble.*.pdb > ensemble.pdb
$bindir/tmclust ensemble.pdb

if [ -e CLUSTER_001.pdb ]; then
    ./qmodope_mainens CLUSTER_001.pdb
else
    ./qmodope_mainens ensemble.pdb
fi

mv best_qdope.pdb final_1.pdb

if [ -e CLUSTER_002.pdb ]; then
    ./qmodope_mainens CLUSTER_002.pdb
    mv best_qdope.pdb final_2.pdb
fi

if [ -e CLUSTER_003.pdb ]; then
    ./qmodope_mainens CLUSTER_003.pdb
    mv best_qdope.pdb final_3.pdb
fi

if [ -e CLUSTER_004.pdb ]; then
    ./qmodope_mainens CLUSTER_004.pdb
    mv best_qdope.pdb final_4.pdb
fi

if [ -e CLUSTER_005.pdb ]; then
    ./qmodope_mainens CLUSTER_005.pdb
    mv best_qdope.pdb final_5.pdb
fi

find . -type f -not \( -name '*map' -or -name '*fasta' -or -name '*.21c' -or -name 'final_*' \) -delete

lenSeq=`wc --chars < $targseq`
lenSeq=$((lenSeq-1))
echo "Sequence with longitude: "$lenSeq
echo ""
echo "end of this prediction"
#TERMINAMOS DE MEDIR EL TIEMPO
fin_ns=`date +%s%N`
fin=`date +%s`
total_ns=$(($fin_ns-$inicio_ns))
total=$(($fin-$inicio))
echo "It has last: -$total_ns- nanoseconds, -$total- seconds"

echo $dirAux > $endFlagdir/$target.txt

rm dope.scr modcheckpot.dat qmodcheck qmodope_mainens