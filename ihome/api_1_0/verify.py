# coding=utf-8

# 验证相关
from flask import request, jsonify
from flask.helpers import make_response

from ihome import redis_strict, constants
from ihome.utils.captcha.captcha import captcha
from ihome.utils.response_code import RET
from . import api


@api.route('/image_code')
def get_image_code():
    """产生图片验证码"""
    # 1.接收参数(图片验证码标识)并进行校验
    image_code_id = request.args.get('cur_id')
    if not image_code_id:
        return jsonify(errno=RET.PARAMERR, errmsg="缺少参数")
    # 2.生成图片验证码
    name, text, content = captcha.generate_captcha()
    # 3.在redis中保存图片验证码
    # redis_store.set("key", "value", "expires")
    try:
        redis_strict.set("imagecode:%s"%image_code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        print e
        return jsonify(errno=RET.DBERR, errmsg="保存图片时出错")

    # 4.返回验证码图片

    response = make_response(content)

    # 指定返回内容的类型
    response.headers["Content-Type"] = "image/jpg"
    return response
