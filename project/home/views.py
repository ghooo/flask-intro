#################
#### imports ####
#################

from project import db # pragma: no cover
from flask import flash, redirect, url_for, render_template, \
		Blueprint, request # pragma: no cover
from forms import MessageForm # pragma: no cover
from flask.ext.login import login_required, current_user # pragma: no cover
from project.models import BlogPost # pragma: no cover

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
) # pragma: no cover

################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST']) # pragma: no cover
@login_required # pragma: no cover
def home():
	error = None
	form = MessageForm(request.form)
	if form.validate_on_submit():
		new_message = BlogPost(
			form.title.data,
			form.description.data,
			current_user.id
		)
		db.session.add(new_message)
		db.session.commit()
		flash('New entry was successfully posted. Thanks.')
		return redirect(url_for('home.home'))
	else:
		posts = db.session.query(BlogPost).all()
		return render_template(
			'index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome') # pragma: no cover
def welcome():
	return render_template('welcome.html')  # render a template

