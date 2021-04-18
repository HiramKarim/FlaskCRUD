class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False