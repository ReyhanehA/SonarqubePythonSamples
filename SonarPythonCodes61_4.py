#    the application doesn’t use the CSRFProtect module:

app = Flask(__name__) # Sensitive: CSRFProtect is missing

@app.route('/')
def hello_world():
    return 'Hello, World!'