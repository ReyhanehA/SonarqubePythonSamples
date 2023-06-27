#Flask

from flask import Response

@app.route('/')
def index():
    response = Response()
    response.set_cookie('key', 'value') # Sensitive
    return response
