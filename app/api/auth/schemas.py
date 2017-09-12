from flask_restplus import fields, Model
__all__ = ['test']
test = Model('a', {
    'a': fields.String,
})
