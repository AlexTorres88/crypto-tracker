from flask import Flask, render_template
from flaskr.methods import add_cryptos, get_prices
from flaskr.settings import *
from flaskr.db_setup import database as db
import datetime

# App definition
app = Flask(__name__, instance_relative_config=True, template_folder='templates')

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.static_folder = 'static'

# Init db
db.init_app(app)

# Filters
@app.template_filter()
def format_datetime(value):
    # Create a python date object to work on
    date_obj = value
    date_obj = datetime.datetime.strptime(date_obj, '%Y-%m-%d %H:%M:%S.%f').strftime('%A %d %B %Y')
    return date_obj
app.jinja_env.filters['format_date'] = format_datetime

# Routes
@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/prices')
def prices():
    res = get_prices()
    # Change string to integer
    add_cryptos(res)
    return render_template('prices.html', coins=res, title="Prices")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
