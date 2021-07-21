from flaskr.__init__ import db

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

    # Relationships
    crypto = db.relationship("Crypto", back_populates="prices", foreign_keys=crypto_id)

    def __init__(self, crypto_id, price, timestamp):
        self.crypto_id = crypto_id
        self.price = price
        self.registered_at = timestamp