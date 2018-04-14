from . import db


class ShoppingCarts(db.Model):
    __tablename__ = 'shopping_cart'
    email = db.Column(db.String(64), primary_key=True)
    thing_info = db.Column(db.String(64))
