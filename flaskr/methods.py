import requests
import datetime
from re import sub
from flaskr.models import Price
from flaskr.settings import CRYPTO_BOT_URL
from flaskr.db_setup import db, session, table_cryptos

def get_prices():
    # Call Azure Function to scrape crypto prices
    res = requests.get(CRYPTO_BOT_URL)
    return res.text

def add_cryptos(res):

    for d in res:
        n = d["name"]

        # Convert price string to numeric
        price = d["price"]
        price  = float(sub(r'[^\d.]', '', price))

        # Convert timestamp string into datetime object
        timestamp = d["timestamp"]
        ts = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

        # Convert market_cap string to numeric
        market_cap = d["market_cap"]
        market_cap = float(sub(r'[^\d.]', '', market_cap))

        # Select crypto_id to insert price
        crypto_id = db.select([table_cryptos.columns.id]).where(table_cryptos.columns.name == n)
        price = Price(crypto_id, price, ts, market_cap)

        # Add records to the db
        session.add(price)
        session.commit()