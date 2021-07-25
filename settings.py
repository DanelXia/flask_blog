class Config(object):
    DEBUG = False
    Testing = False


class Development(Config):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = "test"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
