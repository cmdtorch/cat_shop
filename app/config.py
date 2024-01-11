from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    FLASK_APP = "wsgi.py"
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Database
    DB_NAME = environ.get('DB_NAME')
    DB_USERNAME = environ.get('DB_USERNAME')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_PORT = environ.get('DB_PORT')
    DB_HOST = environ.get('DB_HOST')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}' \
                              f'@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
