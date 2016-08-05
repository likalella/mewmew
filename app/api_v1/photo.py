from flask import request
from flask_restful import Api, Resource, url_for

from sqlalchemy.sql import and_
from sqlalchemy.sql.expression import func

from app.models.photo import PhotoModel
from app.models.user import UserModel


class Photo(Resource):
    def get(self, photo_id):
        return None

    def put(self, photo_id):
        return None

    def delete(self, photo_id):
        return None
