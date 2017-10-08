from flask_restplus import fields, Model

__all__ = ['game_info']
game_info = Model('game_info', {
    'date': fields.String,
    'time': fields.String,
    'vip': fields.Integer,
    'challenger': fields.List(fields.String),
    'be_challenger': fields.List(fields.String)
})
