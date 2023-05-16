from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField,DateField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp, Email

class BasicForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=4, max=25, message="Fname should be between 4-25 chars")])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=4, max=25, message="Lname should be between 4-25 chars")])
    submit = SubmitField('Add Actor')