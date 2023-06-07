For pyjwt module:

jwt.decode(token, verify = False)  # Noncompliant
jwt.decode(token, key, options={"verify_signature": False})  # Noncompliant
----------------------------------------
For python_jwt module:

jwt.process_jwt(token)  # Noncompliant
