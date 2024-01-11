from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app.config.Config")

    db.init_app(app)

    with app.app_context():
        from . import router
        from .model import Cat
        from .utils import create_cats

        db.create_all()
        if not Cat.query.first():
            create_cats()
        return app


