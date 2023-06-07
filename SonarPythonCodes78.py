Django:

CORS_ORIGIN_ALLOW_ALL = True # Sensitive
-----------------------------------------
Flask:

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "True"}}) # Sensitive
-----------------------------------------
User-controlled origin:

origin = request.headers['ORIGIN']
resp = Response()
resp.headers['Access-Control-Allow-Origin'] = origin # Sensitive

