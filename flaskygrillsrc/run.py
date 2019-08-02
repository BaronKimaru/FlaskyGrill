import os
from app import create_app

config_name = os.environ.get('FLASK_ENV')
app = create_app(config_name)


#we dont need to add the below for the app to run
# if __name__ == "__main__":
#     app.run()
