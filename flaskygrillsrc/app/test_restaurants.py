from unittest import TestCase
from app import models

class RestaurantTestCase(TestCase):
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
        response = self.client().post('/restaurants/', data=self.restaurants)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Bhandini", response.data)

    
