from flask import make_response, request

@app.route('/')
def index():
    return make_response(request.args.get("input"))