from flaskr.db_setup import database as db

class Crypto(db.Model):
    __tablename__ = 'cryptos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # Relationships
    prices = db.relationship("Price", back_populates="crypto")

    def __init__(self, name):
        self.name = name

class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    crypto_id = db.Column(db.Integer, db.ForeignKey('cryptos.id'))
    price = db.Column(db.Integer)
    registered_at = db.Column(db.DateTime)
    market_cap = db.Column(db.Integer)

    # Relationships
    crypto = db.relationship("Crypto", back_populates="prices", foreign_keys=crypto_id)

    def __init__(self, crypto_id, price, registered_at, market_cap):
        self.crypto_id = crypto_id
        self.price = price
        self.registered_at = registered_at
        self.market_cap = market_cap
