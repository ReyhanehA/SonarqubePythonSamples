from django.conf import settings

settings.configure(DEBUG=True)  # Sensitive when set to True
settings.configure(DEBUG_PROPAGATE_EXCEPTIONS=True)  # Sensitive when set to True

def custom_config(config):
    settings.configure(default_settings=config, DEBUG=True)  # Sensitive
-----------------------------------------------------------------
Django’s "settings.py" or "global_settings.py" configuration file:

# NOTE: The following code raises issues only if the file is named "settings.py" or "global_settings.py". This is the default
# name of Django configuration file

DEBUG = True  # Sensitive
DEBUG_PROPAGATE_EXCEPTIONS = True  # Sensitive
