from flask import Blueprint
from flask_restful import Api

from app import app

from app.api_v1.document import Document
from app.api_v1.photo import Photo
from app.api_v1.user import User

api = Api()
blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api.init_app(blueprint)

api.add_resource(Document, '/documents/<int:document_id>')
api.add_resource(Photo, '/photos/<int:photo_id>')
api.add_resource(User, '/users/<int:user_id>')
