from . import db


class Orders(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    email = db.Column(db.String(64))
    date = db.Column(db.String(64))
    price = db.Column(db.Float)
    discount = db.Column(db.Float)
    thing_info = db.Column(db.String(512))
    status = db.Column(db.Integer)
    others = db.Column(db.String(1024))
