from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drivesafe.db'
app.config['SECRET_KEY'] = '0674c6086242dd49830f9923'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "secure_payments_page"
# login_manager.login_message_category = "info"


from DriveSafe import routes
