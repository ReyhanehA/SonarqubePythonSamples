#Django

from django.core.mail import send_mail

def send(subject, msg, from_email, to_email):
  send_mail(subject, msg, from_email, [to_email]) # Sensitive