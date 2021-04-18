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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Terminator2027@localhost/dreamteam_db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:HiramCastro20@waterstoredbdev.chfwbtrwgwjv.us-west-1.rds.amazonaws.com/waterstoredbdev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False