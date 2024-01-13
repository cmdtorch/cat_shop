from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from .config import Config


db = SQLAlchemy()


def create_db():
    app_config = Config()
    engine = create_engine(app_config.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app.config.Config")

    create_db()
    db.init_app(app)

    with app.app_context():
        from . import router
        from .model import Cat
        from .utils import create_cats

        db.create_all()
        if not Cat.query.first():
            create_cats()
        return app


