#smtplib

import smtplib

def send(from_email, to_email, msg):
  server = smtplib.SMTP('localhost', 1025)
  server.sendmail(from_email, to_email, msg) # Sensitive
