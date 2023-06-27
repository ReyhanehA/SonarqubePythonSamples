#For a Flask application, the code is sensitive when,

    #the WTF_CSRF_ENABLED setting is set to false:

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False # Sensitive