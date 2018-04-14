from flask_restplus import fields, Model
__all__ = ['modify']

modify = Model('modify_result', {
    'result': fields.Boolean,
    'message': fields.String
})


