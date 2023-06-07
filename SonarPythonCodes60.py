import hashlib
m = hashlib.md5() // Sensitive
---------------------------------
import hashlib
m = hashlib.sha1() // Sensitive
---------------------------------
import md5 // Sensitive and deprecated since Python 2.5; use the hashlib module instead.
m = md5.new()

import sha // Sensitive and deprecated since Python 2.5; use the hashlib module instead.
m = sha.new()
