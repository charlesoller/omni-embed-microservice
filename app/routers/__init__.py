from flask import Blueprint

api = Blueprint('api', __name__)

from app.routers.embedding_router import embed

api.register_blueprint(embed, url_prefix='/embed')

@api.route('/')
def index():
    return "Hello, API!"
