import os


# config.py
class Config(object):
    """Parent configuration"""

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET')


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """Development configuration"""
    DEBUG = False
    TESTING = False


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
