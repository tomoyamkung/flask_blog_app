import os


class DevelopmentConfig(object):
    DEBUG = True
    SECLET_KEY = "secret key"
    USERNAME = "hoge"
    PASSWORD = "password"


class ProductionConfig(object):
    DEBUG = False
    SECLET_KEY = os.environ.get("SERVERLESS_SECRET_KEY")
    USERNAME = "hoge"
    PASSWORD = os.environ.get("SERVERLESS_PASSWORD")
