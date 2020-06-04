import datetime

from flask import abort, current_app, g
from flask_restx import Resource, marshal

from server.business_layers.controllers.work.v1_0.api_work_controller import work_x_api
from server.business_layers.controllers.work.v1_0.models.work import work_model, provider_model
from server.business_layers.injection import work_repo
from server.business_layers.use_cases.work import GetWork

namespace = work_x_api.namespace('work')
namespace.add_model(work_model.name, work_model)
namespace.add_model(provider_model.name, provider_model)


@namespace.route('/<string:iswcs>')
@namespace.response(401, 'unauthorized')
@namespace.response(403, 'forbidden')
class WorkObjectController(Resource):

    @namespace.marshal_with(work_model)
    def get(self, iswcs):
        get_work_use_case = GetWork(work_repo, iswcs.split(';'))
        works = get_work_use_case.execute()

        if not works:
            abort(404)

        return [w.to_dict() for w in works]
