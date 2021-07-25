import requests
from flaskr.models import Price
from flaskr.settings import CRYPTO_BOT_URL
from flaskr.db_setup import db, session, table_cryptos
import datetime
from re import sub

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

        # Conver timestamp string into datetime object
        timestamp = d["timestamp"]
        ts = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

        # Select crypto_id to insert price
        crypto_id = db.select([table_cryptos.columns.id]).where(table_cryptos.columns.name == n)
        price = Price(crypto_id, price, ts)

        # Add records to the db
        session.add(price)
        session.commit()