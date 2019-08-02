from flask import render_template

from . import pages_blueprint       # do not use "from pages impo ... " (otherwise it raises error: 'no module named pages')

@pages_blueprint.route("/")
def index():
    # return "Welcome!"
    return render_template('pages/home.html')


@pages_blueprint.route("/about/")
def about():
    return render_template('pages/about.html')


@pages_blueprint.route("/contact/")
def contact():
    return render_template('pages/contact.html')
