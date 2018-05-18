class Config(object):
    SECRET_KEY = 'hard to guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:110@127.0.0.1:3306/blogdb'
