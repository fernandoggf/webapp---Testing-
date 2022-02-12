from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField, BooleanField 
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

#Python classes will be the representatives of the HTML forms, flask will convert them

class values_debug(FlaskForm):
	url_given = StringField('URL Address (optional)')
	debug = BooleanField('Turn-on Debug?', default=0, validators=[DataRequired(), ])
	submit = SubmitField('ok!')
	