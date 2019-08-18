# Riniker charge sets (`riniker`)

## Reference

> Machine Learning of Partial Charges Derived from High-Quality Quantum-Mechanical Calculations
> Patrick Bleiziffer, Kay Schaller, and Sereina Riniker. 
> J. Chem. Inf. Model.2018583579-590
> https://doi.org/10.1021/acs.jcim.7b00663

## Dataset source

The dataset was downloaded from https://www.research-collection.ethz.ch/handle/20.500.11850/230799

## Dataset composition

* ChEMBL: ~40K molecules
* ZINC: ~90K molecules

## Manifest
* `retrieve.py` - retrieve datasets as compressed SMILES files (`.smi.gz`)
* `ChEMBL.smi.gz` - SMILES for ChEMBL dataset
* `ZINC.smi.gz` - SMILES for ZINC dataset

## Usage

```bash
# Retrieve SMILES datasets
python retrieve.py
# Charge dataset fragmetns
bsub < run-lsf.sh
# Assemble fragments
python assemble.py
```

