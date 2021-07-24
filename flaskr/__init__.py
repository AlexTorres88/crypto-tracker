from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flaskr.methods import *
from flaskr.settings import *
import datetime

# App definition
app = Flask(__name__, instance_relative_config=True, template_folder='../templates')

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.static_folder = '../static'

# Db initialization
db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    app.run()

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
    return render_template('home.html')

@app.route('/prices')
def prices():
    res = get_prices()
    # Change string to integer
    data = json.loads(res)
    add_cryptos(data)
    return render_template('prices.html', coins=data, title="Prices")
    

    