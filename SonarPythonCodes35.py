from OpenSSL import SSL

SSL.Context(SSL.SSLv3_METHOD)  # Noncompliant

import ssl

ssl.SSLContext(ssl.PROTOCOL_SSLv3) # Noncompliant