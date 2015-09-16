# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, \
		flash, g
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

app.secret_key = "no no no no never"
app.database = "sample.db"

# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def home():
	# g is used to store temporary objects like the db, or the user
	g.db = connect_db()
	cur = g.db.execute('SELECT * FROM posts')
	posts = [dict(title=row[0], description=row[1]) \
			for row in cur.fetchall()]
	g.db.close()
	return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or \
				request.form['password'] != 'admin':
			error = 'Invalid credentials. Please retry again.'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('home'))		
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You just logged out!')
	return redirect(url_for('welcome'))


def connect_db():
	return sqlite3.connect(app.database)

if __name__ == '__main__':
	app.run(debug=True)
