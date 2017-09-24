from default import Config
import os


class ProductionConfig(Config):
    # database
    DB_USER_NAME = 'root'
    BD_PASSWORD = '123456'
    URI = 'localhost:3306'
    DATABASE = 'app_basketball_db'
    URL = ''.join(['mysql://', DB_USER_NAME, ':', BD_PASSWORD, '@', URI, '/', DATABASE])

    # sqlalchemy
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xlz'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or URL
