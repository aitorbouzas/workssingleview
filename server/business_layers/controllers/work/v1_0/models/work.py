from flask_restx import Model, fields

provider_model = Model('Provider', {
    'source': fields.String(readonly=True),
    'id': fields.String(readonly=True)
})

work_model = Model('Work', {
    'title': fields.String(readonly=True),
    'contributors': fields.String(readonly=True),
    'iswc': fields.String(readonly=True),
    'providers': fields.List(fields.Nested(provider_model), readonly=True),
})
