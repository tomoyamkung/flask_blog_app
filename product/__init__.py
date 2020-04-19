import os

from flask import Flask
from flask_login import LoginManager

from product.lib.utils import setup_auth
config = {
    "default": "product.config.DevelopmentConfig",
    "development": "product.config.DevelopmentConfig",
    "production": "product.config.ProductionConfig",
}


app = Flask(__name__)
config_name = os.getenv("SERVERLESS_BLOG_CONFIG", "default")
app.config.from_object(config[config_name])

login_manager = LoginManager()
login_manager.init_app(app)

setup_auth(app, login_manager)

from product.views import entries, views  # noqa: E402, F401
from product.views.views import login  # noqa: E402, F401

login_manager.login_view = "login"
login_manager.login_message = "ログインしてください"
