# NCI250K (`nci250k`)

The [NCI250K dataset](https://cactus.nci.nih.gov/download/nci/) contains ~250K small organic molecules of 

## Manifest
* `nci-250k_AM1BCC.oeb` - charged AM1BCC ELF10 dataset

## Usage
```bash
# Retrieve dataset
wget https://cactus.nci.nih.gov/download/nci/NCISMA99.sdz
gzip -dc NCISMA99.sdz | awk '{print $2 " NCI" $1}' | sed "s/\[\([BCNOPSF]\)\]/\1/g" | gzip > nci-250k.smi.gz
# Charge fragments
bsub < run-lsf.sh
# Assemble fragments (when complete)
python assemble.py
```