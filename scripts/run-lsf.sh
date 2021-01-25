#!/usr/bin/env bash
# Set walltime limit
#BSUB -W 6:00
#
# Set output file
#BSUB -o "/home/chodera/charges/stdout/%J-%I.out"
#
# Specify node group
#BSUB -q cpuqueue
#
# Low priority
#BSUB -sp 10
#
##BSUB -m ls-gpu 
##BSUB -m ls-gpu lu-gpu lp-gpu
#
# nodes: number of nodes and GPU request
#BSUB -n 1
#BSUB -R "rusage[mem=2] span[hosts=1]"
#
# job name (default = name of script file)
#BSUB -J "nci250k_am1[1-1000]"
##BSUB -J "ZINC_am1[1-1000]"
##BSUB -J "ChEMBL_am1[1-1000]"

# Make sure to run bashrc
source $HOME/.bashrc

export NJOBS=1000 

# Activate QCFractal conda env
conda activate openeye

# Process fragment
python can_am1_bcc_fragment.py nci-250k.smi.gz nci-250k $LSB_JOBINDEX $NJOBS
#python can_am1_bcc_fragment.py ZINC-riniker.oeb ZINC-AM1BCCELF10 $LSB_JOBINDEX $NJOBS
#python can_am1_bcc_fragment.py ChEMBL-riniker.oeb ChEMBL-AM1BCCELF10 $LSB_JOBINDEX $NJOBS
