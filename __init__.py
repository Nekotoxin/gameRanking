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

    from apps import AuthBP
    app.register_blueprint(AuthBP)

    from apps import GameBP
    app.register_blueprint(GameBP)

    from apps import HomeBP
    app.register_blueprint(HomeBP)

    from apps import MainPageBP
    app.register_blueprint(MainPageBP)

    return app