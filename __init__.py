#文件名：__init__.py
#作用：初始化app，初始化蓝图，初始化数据库
import os
import sys
import click
from flask.cli import FlaskGroup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager,login_user,logout_user,login_required)
WIN = sys.platform.startswith('win')
if WIN: # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else: # 否则使用四个斜线
    prefix = 'sqlite:////'



#向sys添加__init__文件路径
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

db=SQLAlchemy()
login_manager = LoginManager()  # 建立管理器

def create_app():

    app = Flask(__name__,static_folder='apps/static')
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    app.jinja_env.filters['zip'] = zip
    # add jinja round function
    login_manager.init_app(app)
    @login_manager.user_loader
    

    @login_manager.user_loader  # 初始化管理器
    def load_user(user_id):  # 根据user_id返回user对象
        return db_control.find_user(user_id)

    app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db=SQLAlchemy(app)
    # a simple page that says hello
    # @app.route('/')
    # def hello():
    #     return 'Hello, World!'

    from . import db
    db.init_app(app)    


    #注:路由响应不要写在这里 写在对应的蓝图文件里
    #例如   __init__.py:@app.route('/game/<game_id>') (❌) 
    #      /apps/game.py:@GameBP.route('/<game_id>') (✔)   (/game前缀已经添加在了蓝图里)
    #注册蓝图
    from . import db_control
    app.register_blueprint(db_control.cmd)
    #AuthBP:用户注册 登录界面蓝图
    from .apps import auth
    app.register_blueprint(apps.AuthBP)
    #GameBP:单个游戏的页面蓝图
    from .apps import gamepage
    app.register_blueprint(apps.GameBP)
    #UserBP:用户自己主页(功能有修改密码，用户名，放置用户发的感想等)的蓝图
    from .apps import user
    app.register_blueprint(apps.UserBP)
    #MainPageBP:网站主页(展示游戏排行榜)的蓝图
    from .apps import mainpage
    app.register_blueprint(apps.MainPageBP)
    
    return app

