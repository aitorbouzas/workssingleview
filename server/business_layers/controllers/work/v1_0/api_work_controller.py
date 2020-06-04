from flask import Blueprint
from flask_restx import Api

work_api = Blueprint('work_api', __name__, url_prefix='/1.0')

work_x_api = Api(
    work_api,
    validate=True,
    version='1.0',
    title='Work API',
    description='Work API for the management of work single view.',
)
