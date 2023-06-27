#Flask-Mail

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

def send(subject, msg, from_email, to_email):
    mail = Mail(app)
    msg = Message(subject, [to_email], body, sender=from_email)
    mail.send(msg) # Sensitive{code}