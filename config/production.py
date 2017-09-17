from default import Config


class ProductionConfig(Config):
    DB_USER_NAME = 'root'
    BD_PASSWORD = '123456'
    URI = 'localhost:3306'
    DATABASE = 'app_basketball_db'
    URL = ''.join(['mysql://', DB_USER_NAME, ':', BD_PASSWORD, '@', URI, '/', DATABASE])

