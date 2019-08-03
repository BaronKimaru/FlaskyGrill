from flask_api import FlaskAPI
from flask import request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

#local imports
from config import app_config

#initialize
db = SQLAlchemy()

def create_app(config_name):
    #import your model within the create_app
    from app.models import Restaurant

    app = FlaskAPI(__name__, instance_relative_config = True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQL_TRACK_MODIFICATIONS'] = False
    initialize_extensions(app)
    register_blueprints(app)

    @app.route('/restaurants/', methods=['GET','POST'])
    def list_create_restaurants():
        """Either gets all the restaurants or receives & saves restaurant"""
        result = []
        response = None
        try:
            if request.method == "POST":
                print("POST data coming through")

                # take in the data
                name = request.data['name']
                name = str(name)

                # and save it
                if name:
                    restaurant_instance = Restaurant(name=name)
                    restaurant_instance.save()
                    print(f" Instance: {restaurant_instance}")

                    obj = {
                        'id' : restaurant_instance.id,
                        'name': restaurant_instance.name,
                        'date_created': restaurant_instance.date_created,
                        'date_updated': restaurant_instance.date_updated
                    }

                    response = jsonify(obj)         # Always use jsonify(result). never use json.dumps(generates datetime serializable error)
                    response.status_code = 201      # Always use status_code after loading response

                
            else:
                print("GET data coming through")

                restaurants_qs = Restaurant.query.all()
                print(f"restaurant_qs: {restaurants_qs}")
                for restaurant in restaurants_qs:
                    obj = {
                        'id' : restaurant.id,
                        'name': restaurant.name,
                        'date_created': restaurant.date_created,
                        'date_updated': restaurant.date_updated
                    }
                    result.append(obj)
                    
                response = jsonify(result)   # or use jsonify(result)
                response.status_code = 200      # Always use status_code after loading response

        except Exception as e:
            print(f"Exception as: {e}")
            response = str(e)

        finally:
            return response

    return app

def initialize_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    """Registers all the blueprints from different modules with the FlaskAPI app"""
    from app.pages import pages_blueprint
    from app.restaurants import restaurants_blueprint

    app.register_blueprint(pages_blueprint)
    app.register_blueprint(restaurants_blueprint)

    
