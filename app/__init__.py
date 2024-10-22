from flask import Flask
from .config import config
import os

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    from app.routers import api
    app.register_blueprint(api, url_prefix='/api')

    with app.app_context():
        return app