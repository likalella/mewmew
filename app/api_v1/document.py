from flask import request
from flask_restful import Api, Resource, url_for

from sqlalchemy.sql import and_
from sqlalchemy.sql.expression import func

from app.models.document import DocumentModel
from app.models.photo import PhotoModel
from app.models.user import UserModel


class Document(Resource):
    def get(self, document_id):
        return 'get doc'

    def put(self, document_id):
        return None

    def delete(self, document_id):
        return None

