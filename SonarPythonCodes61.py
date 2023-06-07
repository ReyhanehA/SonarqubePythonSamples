For a Django application, the code is sensitive when,

    django.middleware.csrf.CsrfViewMiddleware is not used in the Django settings:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] # Sensitive: django.middleware.csrf.CsrfViewMiddleware is missing
-------------------------------------------------------------
    the CSRF protection is disabled on a view:

@csrf_exempt # Sensitive
def example(request):
    return HttpResponse("default")
-------------------------------------------------------------
For a Flask application, the code is sensitive when,

    the WTF_CSRF_ENABLED setting is set to false:

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False # Sensitive
-------------------------------------------------------------
    the application doesn’t use the CSRFProtect module:

app = Flask(__name__) # Sensitive: CSRFProtect is missing

@app.route('/')
def hello_world():
    return 'Hello, World!'
-------------------------------------------------------------
    the CSRF protection is disabled on a view:

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/example/', methods=['POST'])
@csrf.exempt # Sensitive
def example():
    return 'example '
-------------------------------------------------------------
    the CSRF protection is disabled on a form:

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = False # Sensitive

    name = TextField('name')
    submit = SubmitField('submit')
