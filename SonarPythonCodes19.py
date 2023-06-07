/Flask-SQLAlchemy/

def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:@domain.com" # Noncompliant
------------------------------------------------
/Django/

# settings.py

DATABASES = {
    'postgresql_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickdb',
        'USER': 'sonarsource',
        'PASSWORD': '', # Noncompliant
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
------------------------------------------------
/mysql/mysql-connector-python/

from mysql.connector import connection

connection.MySQLConnection(host='localhost', user='sonarsource', password='')  # Noncompliant