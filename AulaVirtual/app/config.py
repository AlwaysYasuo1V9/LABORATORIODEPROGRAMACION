import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/aulavirtual'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
