# Partial charge datasets for machine learning

This repository contains conformation-independent AM1-BCC ELF10 charge sets Generated using the OpenEye Toolkit 2019.4.2.

Author: John Chodera <john.chodera@choderalab.org>

## License

These datasets are licensed under the Open Data Commons Attribution License (ODC-By) v1.0
https://opendatacommons.org/licenses/by/1-0/index.html

## Manifest

* `environment.yml` - conda environment
* `datasets/` - datasets

## Datasets

Under `dataset/` you will find the following:
* `fda/` - [FDA-approved small molecules](https://zinc.docking.org/substances/subsets/fda/) with ~1.5K molecules
* `riniker/` - [Riniker charge sets](https://www.research-collection.ethz.ch/handle/20.500.11850/230799) with ChEMBL (40K) and ZINC (90K) subsets
* `pdb/` - the [PDB Ligand Expo](http://ligand-expo.rcsb.org/ld-download.html) containing ~23K molecules from the [PDB](http://rcsb.org)
* `nci250k/` - The [NCI250K](https://cactus.nci.nih.gov/download/nci/ set of small organic molecules of interest to drug discovery (~120K)

