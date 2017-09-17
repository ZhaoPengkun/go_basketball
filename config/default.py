import os


class Config(object):

    # base
    APP_NAME = "go_basketball"
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 8088
    basedir = os.path.abspath(os.path.dirname(__file__))

    # database
    DB_USER_NAME = 'root'
    BD_PASSWORD = 'apk.1271'
    URI = 'localhost:33061'
    DATABASE = 'app_basketball_db'
    URL = ''.join(['mysql://', DB_USER_NAME, ':', BD_PASSWORD, '@', URI, '/', DATABASE])

    # sqlalchemy
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xlz'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or URL

    # smtp
    SMTP_HOST = 'smtp.163.com'
    SMTP_PORT = '25'
    SMTP_USERNAME = "go_basketball@163.com"
    SMTP_PASSWORD = "zwx474823"
    SSL_PORT = '587'

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
