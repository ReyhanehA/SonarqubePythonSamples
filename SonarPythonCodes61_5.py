#    the CSRF protection is disabled on a view:

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/example/', methods=['POST'])
@csrf.exempt # Sensitive
def example():
    return 'example '