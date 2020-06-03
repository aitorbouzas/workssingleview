from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from server import config

db = SQLAlchemy()
cache = Cache()


def create_app(package_name=None, register_app_apis=True):
    if not package_name:
        package_name = __name__

    app = Flask(package_name)
    app.url_map.strict_slashes = False

    config.init_app(app)

    # If set to True (the default) Flask-SQLAlchemy will track modifications of objects and emit signals. This requires extra memory and can be disabled if not needed.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # jsonify responses will be output with newlines, spaces, and indentation for easier reading by humans. Always enabled in debug mode.
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    # Register extensions
    register_extensions(app)

    if register_app_apis:
        # Register APIs
        register_apis(app)

    return app


def register_extensions(app):
    """
    Register Flask extensions
    :param app:
    :return: None
    """
    cache.init_app(app, config=app.config.get('CACHE_CONFIG'))
    db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate()
    migrate.init_app(app, db)

    if app.config.get('ENVIRONMENT') == app.config.get('ENVIRONMENT_TYPE_LOCAL') or app.config.get('TESTING'):
        from flask_cors import CORS

        cors = CORS()
        cors.init_app(app)


def register_apis(app):
    """
    Register APIs
    :param app:
    :return: None
    """
    # app.register_blueprint(booking_api)
