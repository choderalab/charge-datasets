#!/usr/bin/env python

"""
Retrieve Riniker datasets and convert to SMILES

source:
https://www.research-collection.ethz.ch/handle/20.500.11850/230799
"""

from openeye import oechem
import os
import urllib.request
import tarfile
from tqdm import tqdm

urls = [
    ('ChEMBL',  'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/230799/ChEMBL_eps_78.tar.gz?sequence=16&isAllowed=y'),
    ('ZINC', 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/230799/ZINC_eps_78.tar.gz?sequence=17&isAllowed=y')
]

class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""
    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize

for (prefix, url) in urls:
    tarfile_filename = f'{prefix}.tgz'
    if not os.path.exists(tarfile_filename):
        print(f'Retrieving {prefix} dataset from {url}...')
        with TqdmUpTo() as t:
            urllib.request.urlretrieve(url, filename=tarfile_filename, reporthook=t.update_to)
    
    # Open output SMILES file for writing
    output_filename = f'{prefix}.smi.gz'
    print(f'Opening {output_filename} for writing SMILES...')
    ofs = oechem.oemolostream()
    if not ofs.open(output_filename):
        oechem.OEThrow.Fatal("Unable to open %s for writing" % output_filename)
    nmolecules = 0

    print(f'Processing {prefix}')
    import tarfile
    tf = tarfile.open(tarfile_filename)
    for name in tqdm(tf.getnames()):
        tf.extract(name)
        ifs = oechem.oemolistream()
        if not ifs.open(name):
            oechem.OEThrow.Fatal("Unable to open %s for reading" % filename)

        for mol in ifs.GetOEMols():
            oechem.OEWriteMolecule(ofs, mol)
            nmolecules += 1

        ifs.close()
        os.remove(name)
    ofs.close()
    print(f'{nmolecules} read')
