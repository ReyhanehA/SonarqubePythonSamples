#crypt

import crypt
from hashlib import pbkdf2_hmac

hash = crypt.crypt(password)         # Noncompliant: salt is not provided