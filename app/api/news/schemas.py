from flask_restplus import fields, Model
__all__ = ['mews', 'video']
mews = Model('news', {
    'url': fields.String,
    'pic': fields.String,
    'title': fields.String
})

video = Model('video', {
    'name': fields.String,
    'url': fields.String,
    'image_src': fields.String
})
