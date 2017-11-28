from os import environ

SECRET_KEY = environ['SECRET_KEY']
DEBUG = environ['DEBUG']
DB_NAME = environ['DB_NAME']
DB_USER = environ['DB_USER']
DB_PASS = environ['DB_PASS']
DB_SERVICE = environ['DB_SERVICE']
DB_PORT = environ['DB_PORT']
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)
