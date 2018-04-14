from . import db


class ShippingAddresses(db.Model):
    __tablename__ = 'shipping_addresses'
    email = db.Column(db.String(64), primary_key=True)
    address_info = db.Column(db.String(256))
