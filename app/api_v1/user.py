from flask import request
from flask_restful import Api, Resource, url_for

from sqlalchemy.sql import and_
from sqlalchemy.sql.expression import func

from app import db

from app.models.user import UserModel


class User(Resource):
    def get(self, user_id):
        return None

    def put(self, user_id):
        return None

    def delete(self, user_id):
        return None
