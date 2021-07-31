import requests
import datetime
from re import sub
import json
from flaskr.models import Crypto, Price
from flaskr.settings import CRYPTO_BOT_URL
from flaskr.db_setup import db, session, table_cryptos
from constants import crypto_symbols

def get_prices():
    res = []
    for coin in crypto_symbols:
        # Get the crypto_id
        crypto = Crypto.query.filter_by(name=coin).first()
        # Get the last price inserted on the db
        p = Price.query.filter_by(crypto_id=crypto.id).order_by(Price.id.desc()).first()
        ans = {}
        ans["name"] = crypto.name
        ans["price"] = p.price
        ans["timestamp"] = p.registered_at
        ans["market_cap"] = p.market_cap
        res.append(ans)
    return res

def add_cryptos(res):
    for d in res:
        # Convert price string to numeric
        price = d["price"]
        price  = float(sub(r'[^\d.]', '', price))

        # Convert timestamp string into datetime object
        timestamp = d["timestamp"]
        ts = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

        # Convert market_cap string to numeric
        market_cap = d["market_cap"]
        market_cap = float(sub(r'[^\d.]', '', market_cap))

        name = d["name"]
        # Select crypto_id to insert price
        crypto_id = db.select([table_cryptos.columns.id]).where(table_cryptos.columns.name == name)
        price = Price(crypto_id, price, ts, market_cap)

        # Add records to the db
        session.add(price)
        session.commit()

def ping_crypto_bot():
    # Call Azure Function to scrape crypto prices
    res = requests.get(CRYPTO_BOT_URL)
    add_cryptos(json.loads(res.text))