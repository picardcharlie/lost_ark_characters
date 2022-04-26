import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "poo_poo_pee_pee"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "la_db.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test_db.sqlite")

config = {"default": Config, "testing": TestingConfig}