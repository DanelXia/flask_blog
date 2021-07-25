from flask import Flask
from settings import Development
from exts import db
from views.blog_view import blog_bp
from views.user_view import user_bp


def create_app():
    app = Flask(__name__,template_folder="../templates")
    app.config.from_object(Development)
    app.config["SECRET_KEY"] = "renyizifuchuan"
    db.init_app(app)
    #注册蓝图
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)
    return app
