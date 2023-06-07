from flask import request
from urllib.request import urlopen

@app.route('/example')
def example():
    url = request.args["url"]
    urlopen(url).read() # Noncompliant