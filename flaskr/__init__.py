from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.methods import *
from flaskr.settings import *

app = Flask(__name__, instance_relative_config=True)

db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    app.run()

@app.route('/prices')
def prices():
    res = get_prices()
    add_cryptos(res)
    return res
    

    