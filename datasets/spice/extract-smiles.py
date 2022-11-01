"""
Extract SMILES from HDF5 file
"""

# TODO: Auto-download SPICE.hdf5 if not present

import h5py
from rich.progress import track
from openff.toolkit.topology import Molecule

hdf5_filename = 'SPICE.hdf5'
smiles_filename = 'spice.smi.gz'
MIN_N_HEAVY = 3 # minimum number of heavy atoms

unique_smiles = dict()

dataset = h5py.File(hdf5_filename, 'r')
for entry_name in track(dataset, description="Extracting SMILES..."):
  entry = dataset[entry_name]
  entry_smiles = entry['smiles'][0].decode("utf-8")
  for smiles in entry_smiles.split('.'):      
      # Canonicalize
      molecule = Molecule.from_smiles(smiles, allow_undefined_stereo=True)
      # Filter
      n_heavy_atoms = len([atom for atom in molecule.atoms if atom.atomic_number > 1])
      if n_heavy_atoms >= MIN_N_HEAVY:      
          smiles = molecule.to_smiles()
          unique_smiles[entry_name] = smiles
 
print(f'There are {len(unique_smiles)} SMILES strings in the file.')

import gzip
with gzip.open(smiles_filename, 'wt') as outfile:
  for title, smiles in unique_smiles.items():
    outfile.write(f'{smiles}\t{title}\n')

