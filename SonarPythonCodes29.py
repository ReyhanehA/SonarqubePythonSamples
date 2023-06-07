pycryptodomex library:

from Cryptodome.Cipher import AES, PKCS1_OAEP,  PKCS1_v1_5
from Cryptodome.Random import get_random_bytes
from Cryptodome.PublicKey import RSA

# Example for a symmetric cipher: AES
AES.new(key, AES.MODE_ECB)  # Noncompliant
AES.new(key, AES.MODE_CBC)  # Noncompliant

# Example for a asymmetric cipher: RSA
cipher = PKCS1_v1_5.new(key) # Noncompliant
-----------------------------------------------
pyca library:

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Example for a symmetric cipher: AES
aes = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())  # Noncompliant
aes = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())  # Noncompliant

# Example for a asymmetric cipher: RSA
ciphertext = public_key.encrypt(
  message,
  padding.PKCS1v15() # Noncompliant
)

plaintext = private_key.decrypt(
  ciphertext,
  padding.PKCS1v15() # Noncompliant
)
-----------------------------------------------
pydes library:

# For DES cipher
des = pyDes.des('ChangeIt') # Noncompliant
des = pyDes.des('ChangeIt', pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) # Noncompliant
des = pyDes.des('ChangeIt', pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) # Noncompliant
-----------------------------------------------
pycrypto library is not maintained and therefore should not be used:

# https://pycrypto.readthedocs.io/en/latest/
from Crypto.Cipher import *
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto.PublicKey import RSA

# Example for a symmetric cipher: AES
AES.new(key, AES.MODE_ECB)  # Noncompliant
AES.new(key, AES.MODE_CBC, IV=iv)  # Noncompliant

# Example for a asymmetric cipher: RSA
cipher = PKCS1_v1_5.new(key) # Noncompliant
