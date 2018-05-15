# coding=utf-8
from . import api
from ihome import redis_strict

@api.route('/', methods=["GET", "POST"])
def hello_world():

    # api.session_cookie_name = 'itheima'
    return 'Hello World!'


