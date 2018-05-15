# coding=utf-8
import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import config_dict
from ihome.api_1_0.index import api

# 创建SQLAlchemy对象
db = SQLAlchemy()


# 工厂方法
def create_app(config_name):

    app = Flask(__name__)
    config_cls = config_dict[config_name]

    app.config.from_object(config_cls)

    db.init_app(app)

    redis_strict = redis.StrictRedis(host=config_cls.REDIS_HOST, port=config_cls.REDIS_PORT)

    # 开启CSRF防护,只做校验
    CSRFProtect(app)

    Session(app)

    app.register_blueprint(api)
    return app