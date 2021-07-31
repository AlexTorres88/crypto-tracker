from flask import Flask, render_template
from flask_login import LoginManager
from flaskr.settings import *
from flaskr.db_setup import database as db
import datetime

# App definition
app = Flask(__name__, instance_relative_config=True, template_folder='templates')

# App configuration
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.static_folder = 'static'

# Init db
db.init_app(app)

# Login management
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from flaskr.models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# Filters
@app.template_filter()
def format_datetime(value):
    # Create a python date object to work on
    date_obj = value
    date_obj = value.strftime('%A %d %B %Y')
    return date_obj
app.jinja_env.filters['format_date'] = format_datetime

# blueprint for auth parts of app
from flaskr.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from flaskr.main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404"), 404
