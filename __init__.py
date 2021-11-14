from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'
    #注册蓝图
    #AuthBP:用户注册 登录界面蓝图
    from apps import AuthBP
    app.register_blueprint(AuthBP)
    #GameBP:单个游戏的页面蓝图
    from apps import GameBP
    app.register_blueprint(GameBP)

    #HomeBP:用户自己主页(功能有修改密码，用户名，放置用户发的感想等)的蓝图
    from apps import HomeBP
    app.register_blueprint(HomeBP)
    #MainPageBP:网站主页(展示游戏排行榜)的蓝图
    from apps import MainPageBP
    app.register_blueprint(MainPageBP)

    return app