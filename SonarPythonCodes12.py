from flask import make_response, request
import json

@app.route('/')
def index():
    json = json.dumps({ "data": request.args.get("input") })
    return make_response(json)