psf/requests library:

import requests

requests.request('GET', 'https://example.domain', verify=False) # Noncompliant
requests.get('https://example.domain', verify=False) # Noncompliant
----------------------------------
Python ssl standard library:

import ssl

ctx1 = ssl._create_unverified_context() # Noncompliant: by default certificate validation is not done
ctx2 = ssl._create_stdlib_context() # Noncompliant: by default certificate validation is not done

ctx3 = ssl.create_default_context()
ctx3.verify_mode = ssl.CERT_NONE # Noncompliant
----------------------------------
pyca/pyopenssl library:

from OpenSSL import SSL

ctx1 = SSL.Context(SSL.TLSv1_2_METHOD) # Noncompliant: by default certificate validation is not done

ctx2 = SSL.Context(SSL.TLSv1_2_METHOD)
ctx2.set_verify(SSL.VERIFY_NONE, verify_callback) # Noncompliant
