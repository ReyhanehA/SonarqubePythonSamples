#Django

from django.core.validators import RegexValidator
from django.urls import re_path

RegexValidator('(a*)*b')  # Sensitive

def define_http_endpoint(view):
    re_path(r'^(a*)*b/$', view)  # Sensitive
