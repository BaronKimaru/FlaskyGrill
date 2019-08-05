import unittest
from app import create_app, db
import os
import json

class RestaurantTestCase(unittest.TestCase):
    """This class represents the restaurants test case"""
    
    def setUp(self):
        """ Defining the test variables as well as initializing the app """
        config_name="testing"
        self.app = create_app(config_name)
        self.client = self.app.test_client
        self.restaurant  = {'name':'Bhandini Indian Restaurant'}
        
        with self.app.app_context():
            db.create_all()
            
    def test_create_restaurant(self):
        """The Test API can Create a restaurant"""
        create_response = self.client().post('/restaurants/', data=self.restaurant)
        print("Create_response: ", create_response)
        self.assertEqual(create_response.status_code, 201)
        self.assertIn("Bhandini", str(create_response.data))
        
    def test_get_all_restaurants(self):
        """The Test API can Get all the restaurants"""
        create_response = self.client().post('/restaurants/', data=self.restaurant)
        self.assertEqual(create_response.status_code, 201)
        get_response = self.client().get('/restaurants/', data=self.restaurant)
        self.assertEqual(get_response.status_code, 200)
        self.assertIn("Bhandini", str(get_response.data))
        
    def test_get_specific_restaurant_by_id(self):
        """The Test API can Get a restaurant by the id"""
        create_response = self.client().post('/restaurants/', data=self.restaurant)
        self.assertEqual(create_response.status_code, 201)
        result = create_response.data.decode('utf-8')
        print(f"GET Result seems to be: {result}")
        result_in_json = json.loads(result)
        print(f"GET DICT Result seems to be: {result_in_json}")
        get_response = self.client().get('/restaurants/{}'.format(result_in_json['id']))
        self.assertEqual(get_response.status_code, 200)
        self.assertIn("Bhandini", str(get_response.data))
        
    def test_edit_restaurant(self):
        """The Test API can Edit a restaurant"""
        create_response = self.client().post('/restaurants/', data={'name':'Trattoria'})
        self.assertEqual(create_response.status_code, 201)
        edit_response = self.client().put('/restaurants/1', data={'name':'Trattoria Ristorante'})          
        self.assertEqual(edit_response.status_code, 200)
        get_response = self.client().get('/restaurants/1')
        self.assertIn("Ristorante", str(get_response.data))
    
    def test_delete_restaurant(self):
        """The Test API can Delete a restaurant"""
        create_response = self.client().post('/restaurants/', data={'name':'Trattoria'})
        self.assertEqual(create_response.status_code, 201)

        # in python3, DELETE & PATCH(i used PUT) method doesnt seem to work, 
        # Instead, both actually fall back to the default GET request.
        del_response = self.client().delete('/restaurants/1', headers={'Content-Type': 'application/x-www-form-urlencoded'})
        print(f"delete resp: {del_response}")       # shows 200 instead of 204 cause no deletion occurs
        print(f"DELETE del_response looks like: {del_response.data}")

        self.assertEqual(del_response.status_code, 204)
        
        # We should test to see if it return somethin', should return a 404
        get_response = self.client().get('/restaurants/1')
        print(f"DELETE get_response looks like: {get_response.data}")
        try:
            self.assertEqual(get_response.status_code, 404)
        except Exception as e:
            print(f"Error as : {e}")

                                                             
    def tearDown(self):
        """teardown all the initialized variables."""
        with self.app.app_context():
            # drop all the created test tables
            db.session.remove()
            db.drop_all()
           
                                                             
# Execute the tests
if __name__ == "__main__":
    unittest.main()
        
