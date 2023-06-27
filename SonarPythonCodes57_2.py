#For zipfile module:

import zipfile

zfile = zipfile.ZipFile('ZipBomb.zip', 'r')
zfile.extractall('./tmp/') # Sensitive
zfile.close()