#!/usr/bin/python3
# encoding: utf-8
import logging

import sentry_sdk
from flask import Flask

from {{cookiecutter.project_slug}}.config import conf

if conf.sentry_dns:  # pragma: no cover
    sentry_sdk.init(
        dsn=conf.sentry_dns,
        traces_sample_rate=1.0
    )

def _register_blueprint(app: Flask) -> None:
    # from {{cookiecutter.project_slug}}.views.xxxx import bp
    # app.register_blueprint(bp)
    pass

def _register_extension(app: Flask) -> None:
    # 数据库初始化
    """
    import redis
    from flask_mongoengine import MongoEngine
    from flask_sqlalchemy import SQLAlchemy
    sql_db = SQLAlchemy(app)
    mongo_db = MongoEngine(app)
    redis_db = redis.Redis.from_url(conf.redis_url)
    """
    pass


logger = logging.getLogger("{{cookiecutter.project_slug}}")
def _register_logger(app: Flask):
    logger.setLevel(app.config.get("LOG_LEVEL", "DEBUG"))

def create_app() -> Flask:
    app = Flask(__name__, static_folder=None)
    app.config.from_object(conf)

    _register_logger(app)
    _register_blueprint(app)
    _register_extension(app)

    return app

