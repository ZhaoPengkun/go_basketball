from . import db


class ChallengerInfo(db.Model):
    __tablename__ = 'challenger_info'
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    challenger = db.Column(db.String(64))
    be_challenger = db.Column(db.String(64))
