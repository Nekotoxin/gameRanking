import os
from flask import Flask

def create_app():
    app = Flask(__name__,static_folder='apps/static')
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    

    # a simple page that says hello
    # @app.route('/')
    # def hello():
    #     return 'Hello, World!'

    from . import db
    #注册蓝图
    #AuthBP:用户注册 登录界面蓝图
    from .apps import auth
    app.register_blueprint(apps.AuthBP)
    #GameBP:单个游戏的页面蓝图
    from .apps import game
    app.register_blueprint(apps.GameBP)
    #UserBP:用户自己主页(功能有修改密码，用户名，放置用户发的感想等)的蓝图
    from .apps import user
    app.register_blueprint(apps.UserBP)
    #MainPageBP:网站主页(展示游戏排行榜)的蓝图
    from .apps import mainpage
    app.register_blueprint(apps.MainPageBP)
    #app.add_url_rule('/', endpoint='mainpage')

    return app