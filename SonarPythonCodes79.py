from django.conf import settings

settings.configure(DEBUG=True)  # Sensitive when set to True
settings.configure(DEBUG_PROPAGATE_EXCEPTIONS=True)  # Sensitive when set to True

def custom_config(config):
    settings.configure(default_settings=config, DEBUG=True)  # Sensitive
