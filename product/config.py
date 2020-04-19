import os


class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = "secret_access_key key"
    USERNAME = "hoge"
    PASSWORD = "password"


class ProductionConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get("SERVERLESS_SECRET_KEY")
    USERNAME = "hoge"
    PASSWORD = os.environ.get("SERVERLESS_PASSWORD")
