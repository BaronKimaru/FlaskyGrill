from flask import Blueprint

# specify name of blueprint 'restaurants' as __name__. specify location of templates
restaurants_blueprint = Blueprint('restaurants', __name__, template_folder="templates", static_folder=None)

from . import views