from . import restaurants_blueprint
from app.models import Restaurant
from flask import jsonify, request, abort
import json


@restaurants_blueprint.route('/restaurants/', methods = ['GET', 'POST'])
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
            print(f"restaurant_qs in GET request: {restaurants_qs}")
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



@restaurants_blueprint.route('/restaurants/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def manipulate_restaurant(id):
    """Either gets one specific restaurant, edits a restaurant instance or deletes specific restaurant"""
    response = None
    restaurant_obj = None
    try:
        restaurant_obj = Restaurant.query.filter_by(id=id).first()
        print(f"Restaurant Instance: {restaurant_obj}")

        if not restaurant_obj:
            abort(404)

        if request.method == 'PUT':
            print("EDIT/PUT data coming through")

            # take in the data
            name = request.data['name']
            name = str(name)

            # and save it
            if name:
                restaurant_obj.name = name
                restaurant_obj.save()

                obj = {
                    'id' : restaurant_obj.id,
                    'name': restaurant_obj.name,
                    'date_created': restaurant_obj.date_created,
                    'date_updated': restaurant_obj.date_updated
                }

                response = jsonify(obj)         # Always use jsonify(result). never use json.dumps(generates datetime serializable error)
                response.status_code = 200      # Always use status_code after loading response

        elif request.method == "DELETE":
            print("DELETE data coming through")
            
            restaurant_obj.delete()
            return {"message": "restaurant {} deleted successfully".format(restaurant_obj.id) 
         }, 200
            
        
        else:
            print("GET data coming through")

            obj = {
                'id' : restaurant_obj.id,
                'name': restaurant_obj.name,
                'date_created': restaurant_obj.date_created,
                'date_updated': restaurant_obj.date_updated
            }
                
            response = jsonify(obj)   # or use jsonify(result)
            response.status_code = 200      # Always use status_code after loading response

    except Exception as e:
        print(f"Exception as: {e}")
        response = str(e)

    finally:
        return response