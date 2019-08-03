from unittest import TestCase
from app import models

class RestaurantTestCase(TestCase):
    def setUp(self):
        config_name="testing"
        self.app = create_app(config_name)
        self.client = self.app.test_client
        self.restaurant  = {'name':'Bhaandini Indian Restaurant'}
        
        with self.app.app_context():
            db.create_all()
