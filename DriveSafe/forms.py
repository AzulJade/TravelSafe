from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,DateField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
# from DriveSafe.models import Route


class CustomerRegister(FlaskForm):
    username = StringField(label = "Username", validators=[Length(min=3, max=30), DataRequired()])
    password1 = PasswordField(label= "Enter Password", validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label = "Resubmit the Password", validators=[EqualTo('password1'), DataRequired()])
    date_of_birth = DateField(label = "Enter your Date of Birth")
    email = StringField(label = "Enter email address:", validators=[Email(), DataRequired()])
    submit = SubmitField(label= "Create your account")

class OwnerRegister(FlaskForm):
    # routes = Route.query.all()
    username = StringField(label = "Username", validators=[Length(min=3, max=30), DataRequired()])
    password1 = PasswordField(label= "Enter Password", validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label = "Resubmit the Password", validators=[EqualTo('password1'), DataRequired()])
    route_id = SelectField('Choose a Route', 
                           choices=[]) # type: ignore
#(routes.id, routes.route_name) for route in routes

class CustomerLogin(FlaskForm):
    username = StringField(label = "Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(Label="Sign in")

class OwnerLogin(FlaskForm):
    username = StringField(label = "Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(Label="Sign in")