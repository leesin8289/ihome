# coding=utf-8
import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import config_dict
from ihome.utils.commons import RegexConverter

# 创建SQLAlchemy对象


db = SQLAlchemy()
redis_strict = None


# 工厂方法
def create_app(config_name):
    app = Flask(__name__)
    config_cls = config_dict[config_name]

    app.config.from_object(config_cls)

    db.init_app(app)

    global redis_strict
    redis_strict = redis.StrictRedis(host=config_cls.REDIS_HOST, port=config_cls.REDIS_PORT)

    # 开启CSRF防护,只做校验
    CSRFProtect(app)

    Session(app)
    app.url_map.converters["re"] = RegexConverter

    from ihome.api_1_0.index import api
    from ihome.web_html import html
    app.register_blueprint(api, url_prefix="/api/v1.0")
    app.register_blueprint(html)

    return app
