from . import db


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    url = db.Column(db.String(512))
    pic = db.Column(db.String(512))
    title = db.Column(db.String(64))
