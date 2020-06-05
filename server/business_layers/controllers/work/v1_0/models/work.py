from flask_restx import Model, fields

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
    'id': fields.Integer(),
    'provider_name': fields.String(),
    'provider_reference': fields.Integer(),
})

work_model = Model('Work', {
    'id': fields.Integer(),
    'title': fields.String(),
    'contributors': fields.String(),
    'iswc': fields.String(),
    'providers': fields.List(fields.Nested(work_provider_model)),
})
