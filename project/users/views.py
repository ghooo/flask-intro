#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
	url_for, Blueprint
from flask.ext.login import login_user, login_required, logout_user
from form import LoginForm
from project.models import User
from project import bcrypt

################
#### config ####
################

users_blueprint = Blueprint(
	'users', __name__,
	template_folder='templates'
)

from project import app, bcrypt

################
#### routes ####
################

# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by( \
                    name=request.form['username']).first()
			if user is not None and bcrypt.check_password_hash(user.password, \
					request.form['password']):
				login_user(user)
				flash('You were logged in.')
				return redirect(url_for('home.home'))
			else:
				error = 'Invalid Credentials. Please try again.'
		else:
			render_template('login.html', form=form, error=error)

	return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You were logged out.')
	return redirect(url_for('home.welcome'))