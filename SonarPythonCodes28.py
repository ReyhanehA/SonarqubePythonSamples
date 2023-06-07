pycryptodomex library:

from Cryptodome.Cipher import DES, DES3, ARC2, ARC4, Blowfish, AES
from Cryptodome.Random import get_random_bytes

key = b'-8B key-'
DES.new(key, DES.MODE_OFB) # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search

key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_CFB) # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack

key = b'Sixteen byte key'
cipher = ARC2.new(key, ARC2.MODE_CFB) # Noncompliant: RC2 is vulnerable to a related-key attack

key = b'Very long and confidential key'
cipher = ARC4.new(key) # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security)

key = b'An arbitrarily long key'
cipher = Blowfish.new(key, Blowfish.MODE_CBC) # Noncompliant: Blowfish use a 64-bit block size makes it vulnerable to birthday attacks
--------------------------------------------
pycryptodome library:

from Crypto.Cipher import DES, DES3, ARC2, ARC4, Blowfish, AES
from Crypto.Random import get_random_bytes

key = b'-8B key-'
DES.new(key, DES.MODE_OFB) # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search

key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_CFB) # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack

key = b'Sixteen byte key'
cipher = ARC2.new(key, ARC2.MODE_CFB) # Noncompliant: RC2 is vulnerable to a related-key attack

key = b'Very long and confidential key'
cipher = ARC4.new(key) # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security)

key = b'An arbitrarily long key'
cipher = Blowfish.new(key, Blowfish.MODE_CBC) # Noncompliant: Blowfish use a 64-bit block size makes it vulnerable to birthday attacks
--------------------------------------------
pyca library:

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom(16)
iv = os.urandom(16)

tdes4 = Cipher(algorithms.TripleDES(key), mode=None, backend=default_backend()) # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack
bf3 = Cipher(algorithms.Blowfish(key), mode=None, backend=default_backend()) # Noncompliant: Blowfish use a 64-bit block size makes it vulnerable to birthday attacks
rc42 = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend()) # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security)
--------------------------------------------
pydes library:

import pyDes;

des1 = pyDes.des('ChangeIt')  # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search
des2 = pyDes.des('ChangeIt', pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search

tdes1 = pyDes.triple_des('ChangeItWithYourKey!!!!!')  # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack
tdes2 = pyDes.triple_des('ChangeItWithYourKey!!!!!', pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack
--------------------------------------------
pycrypto library is not maintained and therefore should not be used:

from Crypto.Cipher import *

des3 = DES.new('ChangeIt') # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search
tdes3 = DES3.new('ChangeItChangeIt') # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack
bf2 = Blowfish.new('ChangeItWithYourKey', Blowfish.MODE_CBC, 'ChangeIt') # Noncompliant: Blowfish use a 64-bit block size makes it
rc21 = ARC2.new('ChangeItWithYourKey', ARC2.MODE_CFB, 'ChangeIt') # Noncompliant: RC2 is vulnerable to a related-key attack
rc41 = ARC4.new('ChangeItWithYourKey') # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security)

