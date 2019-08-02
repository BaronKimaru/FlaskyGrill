from flask import Blueprint

#specify name of blueprint 'pages' as __name__. specify location of templates
pages_blueprint = Blueprint('pages', __name__, template_folder='templates', static_folder=None)

from . import views