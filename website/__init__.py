from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ForbiddenKey'

    from .views import views
    from .auth import auth
    from .diary import diary
    from .macros import macros

    #url prefix is how you access the blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(diary, url_prefix='/')
    app.register_blueprint(macros, url_prefix='/')

    return app
