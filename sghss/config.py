import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost/ProjetoADS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False