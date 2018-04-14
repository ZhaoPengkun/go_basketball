import os


class Config(object):

    # base
    APP_NAME = "go_basketball"
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 8088
    basedir = os.path.abspath(os.path.dirname(__file__))

    # smtp
    SMTP_HOST = 'smtp.163.com'
    SMTP_PORT = '25'
    SMTP_USERNAME = "go_basketball@163.com"
    SMTP_PASSWORD = "zwx474823"
    SSL_PORT = '587'

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    version_id = "1.0"
    app_name = "go_basketball.app"
