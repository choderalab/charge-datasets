#!/usr/bin/env python3

"""
Stitch oeb files together
"""

import sys
import os
from openeye import oechem
from openeye import oeomega
from openeye import oequacpac
import time

for prefix in ['nci-250k']:
    print(f'Assembling {prefix} dataset...')
    filename = prefix + '_AM1BCC.oeb'
    ofs = oechem.oemolostream()
    if not ofs.open(filename):
        oechem.OEThrow.Fatal("Unable to open %s for writing" % argv[2])

    nmolecules = 0
    for index in range(1000):
        filename = prefix + f'-{(index+1):d}.oeb'
        if not os.path.exists(filename): 
            continue
    
        ifs = oechem.oemolistream()
        if not ifs.open(filename):
            oechem.OEThrow.Fatal("Unable to open %s for reading" % filename)

        for mol in ifs.GetOEMols():
            oechem.OEWriteMolecule(ofs, mol)
            nmolecules += 1

        ifs.close()
    print(f'{nmolecules} molecules')

    ofs.close()
