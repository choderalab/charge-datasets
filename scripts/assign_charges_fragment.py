#!/usr/bin/env python3
# (C) 2017 OpenEye Scientific Software Inc. All rights reserved.
#
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of OpenEye products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. OpenEye claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable OpenEye offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED.  OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall OpenEye be
# liable for any damages or liability in connection with the Sample Code
# or its use.

################################################################
# Generates canonical AM1-BCC charges
################################################################

import sys
from openeye import oechem
from openff.toolkit.topology import Molecule
import time

def main(argv=[__name__]):
    if len(argv) != 5:
        oechem.OEThrow.Usage("%s <infile> <outfile> <frag> <nfrags>" % argv[0])

    frag = int(argv[3])
    nfrags = int(argv[4])

    if frag == 0:
        oechem.OEThrow.Fatal("<frag> must start at 1")

    # Count number of molecules
    ifs = oechem.oemolistream()
    if not ifs.open(argv[1]):
        oechem.OEThrow.Fatal("Unable to open %s for reading" % argv[1])
    nmolecules = 0
    for mol in ifs.GetOEMols():
        nmolecules += 1
    ifs.close()
    
    # Open for reading
    ifs = oechem.oemolistream()
    if not ifs.open(argv[1]):
        oechem.OEThrow.Fatal("Unable to open %s for reading" % argv[1])
    
    nstart = int( (nmolecules / nfrags) * (frag-1) )
    nprocess = min( nmolecules, int( (nmolecules / nfrags) * frag ) - int( (nmolecules / nfrags) * (frag-1) ) )


    #if not oechem.OEIs3DFormat(ifs.GetFormat()):
    #    oechem.OEThrow.Fatal("Invalid input format: need 3D coordinates")

    # Open file for writing
    ofs = oechem.oemolostream()
    if not ofs.open(argv[2] + f'.{frag:05d}.oeb'):
        oechem.OEThrow.Fatal("Unable to open %s for writing" % argv[2])

    if ofs.GetFormat() not in [oechem.OEFormat_MOL2, oechem.OEFormat_OEB]:
        oechem.OEThrow.Error("MOL2 or OEB output file is required!")

    print(f'Fragment {frag} of {nfrags} : Starting at molecule {nstart} and processing {nprocess} molecules from {argv[1]} to write to {argv[2]}')

    for index, oemol in enumerate(ifs.GetOEMols()):
        if (index < nstart) or (index >= nstart+nprocess):
            continue

        smiles = oechem.OEMolToSmiles(oemol)

        print(f'Processing {index} in range {nstart}:{nstart+nprocess} ({(index - nstart) / nprocess * 100.0}%)')

        # Use openff toolkit to assign canonical AM1-BCC charges
        initial_time = time.time()            
        print(smiles)
        try:
            offmol = Molecule.from_smiles(smiles, allow_undefined_stereo=True)
            for protomer in offmol.enumerate_protomers():
                for tautomer in offmol.enumerate_tautomers():
                    for stereoisomer in offmol.enumerate_stereoisomers():
                
                        stereoisomer.compute_partial_charges_am1bcc()
                        oemol = offmol.to_openeye()
                        
                        oechem.OEWriteMolecule(ofs, oemol)
                        nmolecules += 1
            
            total_time = time.time() - initial_time
            average_time = total_time / nmolecules
            print(f'{nmolecules} molecules processed in {total_time} seconds : {average_time} seconds/molecule')
        except Exception as e:
            print(e)
            print(f"Failed to generate conformation(s) for molecule {oemol.GetTitle()} {smiles}")
            
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
