from flask_caching import Cache
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cache = Cache()
migrate = Migrate(directory='/var/server/migrations')
cors = CORS()
