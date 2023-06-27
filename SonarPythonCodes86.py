#cryptography module

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESCCM
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher


def encrypt(key):
    Fernet(key)  # Sensitive
    ChaCha20Poly1305(key)  # Sensitive
    AESGCM(key)  # Sensitive
    AESCCM(key)  # Sensitive


private_key = rsa.generate_private_key()  # Sensitive


def encrypt2(algorithm, mode, backend):
    Cipher(algorithm, mode, backend)  # Sensitive
