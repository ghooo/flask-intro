#################
#### imports ####
#################

from project import app, db
from flask import flash, redirect, session, url_for, render_template, \
		Blueprint
from functools import wraps
from flask.ext.login import login_required

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
	# return "Hello, World!"  # return a string
	from project.models import BlogPost
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)  # render a template


@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html')  # render a template

