from flask_restplus import fields, Model
__all__ = ['order', 'result']

order = Model('order', {
    'order_id': fields.Integer,
    'result': fields.String,
    'message': fields.String,
    'email': fields.String,
    'date': fields.String,
    'price': fields.Float,
    'thing_info': fields.String,
    'status': fields.Integer
})

result = Model('result', {
    'result': fields.String,
    'message': fields.String
})
