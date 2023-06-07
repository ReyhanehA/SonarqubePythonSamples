from flask import request
import requests

@app.route('/example')
def example():
    url = request.args["url"]
    requests.get(url).content # Noncompliant