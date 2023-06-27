#For a Django application, the code is sensitive when,

    #django.middleware.csrf.CsrfViewMiddleware is not used in the Django settings:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] # Sensitive: django.middleware.csrf.CsrfViewMiddleware is missing