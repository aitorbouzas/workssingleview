from flask import abort
from flask_restx import Resource

from server.business_layers.controllers.work.v1_0.api_work_controller import work_x_api
from server.business_layers.controllers.work.v1_0.models.work import work_model, work_provider_model, work_post_model, work_provider_post_model
from server.business_layers.injection import work_repo, provider_repo
from server.business_layers.use_cases.work import GetWork, PostWork

namespace = work_x_api.namespace('work')
namespace.add_model(work_model.name, work_model)
namespace.add_model(work_provider_model.name, work_provider_model)
namespace.add_model(work_post_model.name, work_post_model)
namespace.add_model(work_provider_post_model.name, work_provider_post_model)


@namespace.route('/')
class WorkController(Resource):
    @namespace.expect(work_post_model)
    @namespace.marshal_with(work_model)
    def post(self):
        payload = namespace.payload
        post_work_use_case = PostWork(work_repo, provider_repo, payload)
        new_work = post_work_use_case.execute()
        return new_work.to_dict() if new_work else None


@namespace.route('/<string:iswcs>')
@namespace.response(404, 'notfound')
class WorkObjectController(Resource):

    @namespace.marshal_with(work_model)
    def get(self, iswcs):
        get_work_use_case = GetWork(work_repo, iswcs.split(';'))
        works = get_work_use_case.execute()

        if not works:
            abort(404)

        return [w.to_dict() for w in works]
