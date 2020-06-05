from flask_restx import Model, fields
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

work_provider_post_model = Model('WorkProviderPost', {
    'source': fields.String(),
    'id': fields.String()
})

work_post_model = Model('WorkPost', {
    'title': fields.String(),
    'contributors': fields.String(),
    'iswc': fields.String(),
    'providers': fields.List(fields.Nested(work_provider_post_model)),
})

work_provider_model = Model('WorkProvider', {
    'provider_name': fields.String(),
    'provider_reference': fields.Integer(),
})

work_model = Model('Work', {
    'title': fields.String(),
    'contributors': fields.String(),
    'iswc': fields.String(),
    'providers': fields.List(fields.Nested(work_provider_model)),
})


upload_model = RequestParser()
upload_model.add_argument('file', location='files', type=FileStorage, required=True)
