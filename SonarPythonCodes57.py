#For tarfile module:

import tarfile

tfile = tarfile.open("TarBomb.tar")
tfile.extractall('./tmp/')  # Sensitive
tfile.close()
