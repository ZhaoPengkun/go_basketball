from flask_restplus import fields, Model
__all__ = ['mews']
mews = Model('news', {
    'url': fields.String,
    'pic': fields.String,
    'title': fields.String
})
