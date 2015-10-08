from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class MessageForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextField('Description', validators=[DataRequired(), \
			Length(max=140)])
