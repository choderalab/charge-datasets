# AM1-BCC charges for the SPICE dataset

This is a set of AM1-BCC ELF10 charges prepared using `openff.toolkit.topology.Molecule.assign_am1bcc_charges` from the OpenFF Toolkit 0.10.6 and OpenEye Toolkit 2022.1.1.
Prepared from [SPICE 1.0](https://github.com/openmm/spice-dataset/releases/tag/1.0) 

## Manifest
* `spice.mol2` - mol2 format of molecules with charges
* `spice.oeb` - OpenEye Toolkit oeb format of molecules with charges
* `spice.smi.gz` - extracted SMILES of all molecules >= 3 heavy atoms
* `extract-smiles.py` - simple script to strip SMILES from SPICE.hdf5 file
* `environment.yml` - conda environment used to generate this data

## Extracting charges

### With the OpenEye toolkit

```python
from openeye import oechem
with oechem.oemolistream('spice.oeb') as ifs:
for index, oemol in enumerate(ifs.GetOEMols()):
    # Iterate over atoms
    # Atom properties: https://docs.eyesopen.com/toolkits/python/oechemtk/atomproperties.html
    for oeatom in oemol.GetAtoms():
        atom_index = oeatom.GetIdx() # not guaranteed to come out in order
        charge = oeatom.GetPartialCharge()
    # Iterate over bonds
    # Bond properties: https://docs.eyesopen.com/toolkits/python/oechemtk/bondproperties.html
    for oebond in oemol.GetBonds():
        atom_index_1 = oebond.GetBgn().GetIdx()
	atom_index_2 = oebond.GetEnd().GetIdx()
	bond_order = oebond.GetOrder()
```

### With the Open Force Field Toolkit

(Note that this requires the OpenEye Toolkit to be installed to support reading mol2 files; RDKit does not support this)

```python
from openff.toolkit.topology import Molecule

molecules = Molecule.from_file('spice.mol2')
for molecule in molecules:
    partial_charges = molecule.partial_charges # this is a Quantity wrapped array (I think?)
```

