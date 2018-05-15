# coding=utf-8
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from ihome import create_app, db

app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


# @app.route('/', methods=["GET", "POST"])
# def hello_world():
#
#     app.session_cookie_name = 'itheima'
#     return 'Hello World!'


if __name__ == '__main__':
    manager.run()
