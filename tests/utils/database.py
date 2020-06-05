from flask_migrate import upgrade as flask_migrate_upgrade
from sqlalchemy_utils import create_database, database_exists, drop_database

from tests.fixtures.database import populate


def drop(app):
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI')

    if database_exists(db_uri):
        drop_database(db_uri)


def create(app):
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI')

    if not database_exists(db_uri):
        create_database(db_uri)
        flask_migrate_upgrade()
        populate()
