#User-controlled origin:

origin = request.headers['ORIGIN']
resp = Response()
resp.headers['Access-Control-Allow-Origin'] = origin # Sensitive