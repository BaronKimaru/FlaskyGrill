from flask_api import FlaskAPI
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#local imports
from config import app_config

#initialize
db = SQLAlchemy()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config = True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQL_TRACK_MODIFICATIONS'] = False
    initialize_extensions(app)
    register_blueprints(app)
    return app

def initialize_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    """Registers all the blueprints from different modules with the FlaskAPI app"""
    from app.pages import pages_blueprint

    app.register_blueprint(pages_blueprint)

    
