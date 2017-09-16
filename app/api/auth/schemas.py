from flask_restplus import fields, Model
__all__ = ['register']
register = Model('register_result', {
    'register_result': fields.String,
})

login = Model('login_result', {
    'login_result': fields.String,
})
