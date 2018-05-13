# coding=utf-8
import redis


class Config(object):
    DEBUG = True

    SECRET_KEY = "ZP4HpC0vRsT2F15gAuVbN41WoBQeGsPQ0OOem7bE3Utf/d2tLaonv/tfklyVPxQJ"

    # mysql配置
    # 设置数据库的链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    # 关闭追踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis数据库的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # sission存储配置
    # 设置session信息存储到redis数据库中
    SESSION_TYPE = "redis"
    # 设置session存储到哪个数据库中
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启session签名（加密）
    SESSION_USE_SINGNER = True
    # 设置session过期时间
    PERMANENT_SESSION_LIFETIME = 3360


class DevelopmentConfig(Config):
    """开发环境中配置类"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境中的配置类"""
    pass


config_dict = {
    "development": DevelopmentConfig,
}
