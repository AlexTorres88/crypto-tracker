from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flaskr.methods import get_prices, ping_crypto_bot
from constants import crypto_names

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html', title="Home")

@main.route('/prices')
def prices():
    # ping_crypto_bot()
    res = get_prices()
    return render_template('prices.html', coins=res, coin_names=crypto_names, title="Prices")

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title="Profile", name=current_user.name)