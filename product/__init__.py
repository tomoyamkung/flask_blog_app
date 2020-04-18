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


login_manager.login_view = "login"
login_manager.login_message = "ログインしてください"
