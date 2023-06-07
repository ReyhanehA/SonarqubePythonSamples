For tarfile module:

import tarfile

tfile = tarfile.open("TarBomb.tar")
tfile.extractall('./tmp/')  # Sensitive
tfile.close()
---------------------------------------------
For zipfile module:

import zipfile

zfile = zipfile.ZipFile('ZipBomb.zip', 'r')
zfile.extractall('./tmp/') # Sensitive
zfile.close()
