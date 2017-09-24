from flask_restplus import fields, Model
__all__ = ['register', 'login', 'verification']
register = Model('register_result', {
    'register_result': fields.String,
})

login = Model('login_result', {
    'login_result': fields.String,
})

verification = Model('verification_code', {
    'verification_code': fields.String,
})
