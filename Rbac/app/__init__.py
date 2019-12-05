import os
from flask import Flask

from app.api import api
from app.config import config
from app.views.hello import hello_bp
from app.cli import register_cli
from app.extension import mongo
from app.logger import register_logging

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('app')
    app.config.from_object(config[config_name])

    register_extensions(app)  
    register_views(app)  
    register_cli(app)
    register_shell_context(app)
    register_logging(app)

    return app


def register_views(app):
    # app.register_blueprint(hello_bp, url_prefix='/hello/')
    app.register_blueprint(hello_bp)
    app.register_blueprint(api)


def register_extensions(app):
    mongo.init_app(app)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(mongo=mongo)