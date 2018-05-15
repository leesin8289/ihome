# coding=utf-8
from . import api


@api.route('/', methods=["GET", "POST"])
def hello_world():

    api.session_cookie_name = 'itheima'
    return 'Hello World!'


