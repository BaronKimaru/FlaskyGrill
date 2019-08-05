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
        response = self.client().post('/restaurants/', data=self.restaurant)
        print("response:", response)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Bhandini", str(response.data))
        
    def test_get_all_restaurants(self):
        """The Test API can Get all the restaurants"""
        response = self.client().post('/restaurants/', data=self.restaurant)
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/restaurants/', data=self.restaurant)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Bhandini", str(response.data))
        
    def test_get_specific_restaurant_by_id(self):
        """The Test API can Get a restaurant by the id"""
        response = self.client().post('/restaurants/', data=self.restaurant)
        self.assertEqual(response.status_code, 201)
        result = response.data.decode('utf-8')
        print(f"Result seems to be: {result}")
        result_in_json = json.loads(result)
        response = self.client().get('/restaurants/{}'.format(result_in_json['id']))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Bhandini", str(response.data))
        
    def test_edit_restaurant(self):
        """The Test API can Edit a restaurant"""
        response = self.client().post('/restaurants/', data={'name':'Trattoria'})
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/restaurants/1', data={'name':'Trattoria Ristorante'})          
        self.assertEqual(response.status_code, 200)
        get_response = self.client().get('/restaurants/1')
        self.assertIn("Ristorante", str(get_response.data))
    
    def test_delete_restaurant(self):
        """The Test API can Delete a restaurant"""
        create_response = self.client().post('/restaurants/', data={'name':'Trattoria'})
        self.assertEqual(create_response.status_code, 201)
        del_response = self.client().delete('/restaurants/1')          
        self.assertEqual(del_response.status_code, 200)
        get_response = self.client().get('/restaurants/1')
        self.assertEqual(get_response.status_code, 404)
                                                             
    def tearDown(self):
        """teardown all the initialized variables."""
        with self.app.app_context():
            # drop all the created test tables
            db.session.remove()
            db.drop_all()
           
                                                             
# Execute the tests
if __name__ == "__main__":
    unittest.main()
        
