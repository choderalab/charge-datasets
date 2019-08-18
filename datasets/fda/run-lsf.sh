#!/usr/bin/env bash
# Set walltime limit
#BSUB -W 6:00
#
# Specify node group
#BSUB -q cpuqueue
#
# Low priority
#BSUB -sp 10
#
# nodes: number of nodes and GPU request
#BSUB -n 1
#BSUB -R "rusage[mem=2] span[hosts=1]"
#
# job name (default = name of script file)
#BSUB -J "fda[1-100]"

# Make sure to run bashrc
source $HOME/.bashrc

export NJOBS=100

# Activate QCFractal conda env
conda activate openeye

# Process dataset fragment
for PREFIX in "fda"
do
  python charge.py $PREFIX.smi.gz $PREFIX-${LSB_JOBINDEX}.oeb $LSB_JOBINDEX $NJOBS
done

