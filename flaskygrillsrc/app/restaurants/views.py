from . import restaurants_blueprint
from app.models import Restaurant
from flask import jsonify, request
import json


# @restaurants_blueprint('/restaurants/', methods = ['GET', 'POST'])
# @app.route('/restaurants/', methods=['GET','POST'])
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

        