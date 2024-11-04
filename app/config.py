import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost:3306/lucas"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Clave secreta para Flask-WTF
