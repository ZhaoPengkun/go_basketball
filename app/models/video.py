from . import db


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    url = db.Column(db.String(512))
    name = db.Column(db.String(512))
    image_src = db.Column(db.String(512))

