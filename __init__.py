#文件名：__init__.py
#作用：初始化app，初始化蓝图，初始化数据库
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



    #注:路由响应不要写在这里 写在对应的蓝图文件里
    #例如   __init__.py:@app.route('/game/<game_id>') (❌) 
    #      /apps/game.py:@GameBP.route('/<game_id>') (✔)   (/game前缀已经添加在了蓝图里)
    from . import db
    db.init_app(app)
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
    
    return app