import os 

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    SECRET_KEY = 'PassWdntid&&dddgy234256dsbbdaafssd2dddd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')

class ProductionConfig(Config):
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI') or \
                               'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig, 
    'production': ProductionConfig, 
    'default': DevelopmentConfig
}