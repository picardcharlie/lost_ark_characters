from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

from . import main
from . import auth
from . import character

bootstrap = Bootstrap()


def create_app(config_name = "testing"):
    app = Flask(__name__)

    # import config settings
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #initilize extensions
    bootstrap.init_app(app)

    from app.models import db
    db.init_app(app)

    # register blueprints
    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth)

    #from .character import character

    return app