#!/usr/bin/env python

from openeye import oechem
import os

prefix = 'ZINC'
prefix = 'ChEMBL'
input_directory = f'{prefix}_mols'
output_filename = f'{prefix}-riniker.oeb'

# Open output file for writing
ofs = oechem.oemolostream()
if not ofs.open(output_filename):
    oechem.OEThrow.Fatal("Unable to open %s for writing" % output_filename)

nmolecules = 0

filenames = os.listdir(input_directory)
for filename in filenames:
    print(filename)
    ifs = oechem.oemolistream()
    if not ifs.open(os.path.join(input_directory, filename)):
        oechem.OEThrow.Fatal("Unable to open %s for reading" % filename)

    #ifs.SetFormat(oechem.OEFormat_SDF)

    for mol in ifs.GetOEMols():
        #for atom in mol.GetAtoms():
        #    print(atom.GetPartialCharge())
        oechem.OEWriteMolecule(ofs, mol)
        nmolecules += 1

    ifs.close()
ofs.close()
print(f'{nmolecules} read')
