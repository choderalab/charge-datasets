# PDB Ligand Expo (`pdb`)

The [PDB Ligand Expo](http://ligand-expo.rcsb.org/ld-download.html) contains all recurring molecular entities found in the PDB.
Individual polymeric residues are capped in this dataset.

source: http://ligand-expo.rcsb.org/dictionaries/Components-smiles-stereo-oe.smi

## Manifest

## Usage

```bash
# Retrieve data
wget http://ligand-expo.rcsb.org/dictionaries/Components-smiles-stereo-oe.smi
mv Components-smiles-stereo-oe.smi pdb.smi
gzip pdb.smi
# Charge dataset fragmetns
bsub < run-lsf.sh
# Assemble fragments when complete (deleting fragments)
python assemble.py
```