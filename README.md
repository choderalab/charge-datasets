# Partial charge datasets for machine learning

This repository contains conformation-independent AM1-BCC ELF10 charge sets Generated using the OpenEye Toolkit 2019.4.2.

Author: John Chodera <john.chodera@choderalab.org>

## License

These datasets are licensed under the Open Data Commons Attribution License (ODC-By) v1.0
https://opendatacommons.org/licenses/by/1-0/index.html

## Manifest

* `environment.yml` - conda environment
* `scripts/` - scripts to generate charge datasets
* `datasets/` - datasets

## Scripts

* `run-lsf.sh` - LSF submission script using job arrays
* `convert.py` - script to convert directory of .mol2 files into single .oeb file
* `charge.py` - generate .oeb file containing AM1-BCC charges for a shard of input .oeb file
* `compile.py` - compile .oeb shards into a single .oeb file

## Datasets

### FDA-approved small molecules (`fda`)

source: https://zinc.docking.org/substances/subsets/fda/

### Riniker charge sets (`riniker`)

source: https://www.research-collection.ethz.ch/handle/20.500.11850/230799

* ChEMBL - 40K
* ZINC - 90K 

### PDB Ligand Expo (`pdb`)

http://ligand-expo.rcsb.org/ld-download.html

source: http://ligand-expo.rcsb.org/dictionaries/Components-smiles-stereo-oe.smi

### NCI250K (`nci250k`)

The NCI250K dataset was retrieve from https://cactus.nci.nih.gov/download/nci/ and processed into a SMILES file by:
```
wget https://cactus.nci.nih.gov/download/nci/NCISMA99.sdz
gzip -dc NCISMA99.sdz | awk '{print $2 " NCI" $1}' | sed "s/\[\([BCNOPSF]\)\]/\1/g" | gzip > nci-250k.smi.gz
```

