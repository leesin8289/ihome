# coding=utf-8

from flask import Blueprint
from flask import current_app

html = Blueprint('html', __name__)


@html.route("/<re('.*'):file_name>")
def get_static_html(file_name):
    # print 123131

    if file_name == "":
        file_name = "index.html"

    if file_name != "favicon.ico":
        file_name = "html/" + file_name

    # print file_name
    return current_app.send_static_file(file_name)