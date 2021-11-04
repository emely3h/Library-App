from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message= 'field can not be empty'), Email(message='Email adress not valid')])
    password = PasswordField('Password', validators=[DataRequired(message= 'field can not be empty')])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(message= 'field can not be empty')])
    email = StringField('Email:', validators=[DataRequired(message= 'field can not be empty'), Email(message='Email adress not valid')])
    password = PasswordField('Password:', validators=[DataRequired(message='field can not be empty')])
    confirm_password = PasswordField('Confirm password:', validators=[DataRequired(message= 'field can not be empty'), EqualTo('password', message='passwords have to match')])
    submit = SubmitField('Submit')
class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message= 'field can not be empty')])
    author = StringField('Author', validators=[DataRequired(message= 'field can not be empty')])
    description = TextAreaField('Description', validators=[DataRequired(message= 'field can not be empty')])
    submit = SubmitField('Add Book')