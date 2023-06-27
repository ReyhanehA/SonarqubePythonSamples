#pynacl library

from nacl.public import Box
from nacl.secret import SecretBox


def public_encrypt(secret_key, public_key):
    Box(secret_key, public_key)  # Sensitive


def secret_encrypt(key):
    SecretBox(key)  # Sensitive