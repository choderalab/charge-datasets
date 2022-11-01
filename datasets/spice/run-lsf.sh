#!/bin/bash
#
# Prepare all transformations
#

# job name (default = name of script file)
#BSUB -J "spice_am1[1-100]"
##BSUB -J "nci250k_am1[1-1000]"
##BSUB -J "ZINC_am1[1-1000]"
##BSUB -J "ChEMBL_am1[1-1000]"
#
#BSUB -o %J_%I.stdout 
#BSUB -eo %J_%I.stderr
#BSUB -L /bin/bash
#
#BSUB -W 6:00
#
# Set output file
#BSUB -oe "%J-%I.out"
#
# Specify node group
#BSUB -q cpuqueue
#
# Low priority
#BSUB -sp 10
#
#
# nodes: number of nodes and GPU request
#BSUB -n 1
#BSUB -R "rusage[mem=4] span[hosts=1]"
#

# Make sure to run bashrc
source $HOME/.bashrc

#export NJOBS=1000 
export NJOBS=100

conda activate openeye

# Process fragment
export FRAGMENT=$(expr $LSB_JOBINDEX + 0) # RUN is zero-indexed
python ../../scripts/can_am1_bcc_fragment.py spice.smi.gz spice $FRAGMENT $NJOBS
#python can_am1_bcc_fragment.py nci-250k.smi.gz nci-250k $FRAGMENT $NJOBS
#python can_am1_bcc_fragment.py ZINC-riniker.oeb ZINC-AM1BCCELF10 $FRAGMENT $NJOBS
#python can_am1_bcc_fragment.py ChEMBL-riniker.oeb ChEMBL-AM1BCCELF10 $FRAGMENT $NJOBS
