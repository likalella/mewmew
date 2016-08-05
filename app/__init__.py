from flask import Flask, url_for
from flask.ext.marshmallow import Marshmallow
from flask.ext.sqlalchemy import SQLAlchemy


from config import config

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow()

from app.models import *
from app.routes import *
from app.api_v1 import *


def create_app(config_name):

    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://mewmew:mewmew16@localhost/mewmew'

    db.init_app(app)
    db.app=app
    ma.init_app(app)
    db.create_all()

    app.register_blueprint(blueprint)

    return app
