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

# Determine prefixes to assembl
import glob
import re
filenames = glob.glob("*-*.oeb")
prefixes = set()
for filename in filenames:
    match = re.match('(\w+)-\d+.oeb', filename)
    if match:
        prefix = match.group(1)
        prefixes.add(prefix)
print(prefixes)

for prefix in prefixes:
    print(f'Assembling {prefix} dataset and deleting original fragments...')
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
        os.unlink(filename)
    print(f'{nmolecules} molecules')

    ofs.close()
