smtplib

import smtplib

def send(from_email, to_email, msg):
  server = smtplib.SMTP('localhost', 1025)
  server.sendmail(from_email, to_email, msg) # Sensitive
-----------------------------------
Django

from django.core.mail import send_mail

def send(subject, msg, from_email, to_email):
  send_mail(subject, msg, from_email, [to_email]) # Sensitive
-----------------------------------
Flask-Mail

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

def send(subject, msg, from_email, to_email):
    mail = Mail(app)
    msg = Message(subject, [to_email], body, sender=from_email)
    mail.send(msg) # Sensitive{code}
