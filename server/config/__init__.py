import os

from werkzeug.utils import import_string


def init_app(app, testing=False):
    ENVIRONMENT = os.getenv('ENVIRONMENT', False)
    if not ENVIRONMENT:
        raise Exception('DANGER: Please define ENVIRONMENT in environment variables!')

    # load file config: app/config/ENVIRONMENT.py
    file_config = import_string(f'server.config.{ENVIRONMENT.lower()}')

    app.debug = file_config.DEBUG
    app.config["SQLALCHEMY_DATABASE_URI"] = file_config.DB_URI if not testing else file_config.TEST_DB_URI
    app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"
        ] = file_config.SQLALCHEMY_TRACK_MODIFICATIONS
