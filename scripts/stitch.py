#!/usr/bin/env python3

"""
Stitch oeb files together

usage:

python stitch.py <prefix>
"""

import sys
from openeye import oechem
from openeye import oeomega
from openeye import oequacpac
import time

prefix = sys.argv[1]
#prefix = 'nci-250k'
#prefix = 'ZINC-AM1BCCELF10'
#prefix = 'ChEMBL-AM1BCCELF10'
filename = prefix + '.oeb'
ofs = oechem.oemolostream()
if not ofs.open(filename):
    oechem.OEThrow.Fatal("Unable to open %s for writing" % filename)

# TODO: Auto-detect how many fragments there are with this prefix

nmolecules = 0
for index in range(100):
    filename = prefix + f'.{(index+1):05d}.oeb'
    print(filename)
    ifs = oechem.oemolistream()
    if not ifs.open(filename):
        oechem.OEThrow.Fatal("Unable to open %s for reading" % filename)

    for mol in ifs.GetOEMols():
        oechem.OEWriteMolecule(ofs, mol)
        nmolecules += 1

    ifs.close()
    print(f'{nmolecules} molecules')

ofs.close()
