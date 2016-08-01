import sys

from flask import Flask
from flask.ext.marshmallow import Marshmallow
from flask.ext.sqlalchemy import SQLAlchemy

from config import config


db = SQLAlchemy()
ma = Marshmallow()

from app.models import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://mewmew:mewmew16@localhost/mewmew'

    db.init_app(app)
    db.app=app
    ma.init_app(app)

    db.create_all()

    from .api_v1 import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app
