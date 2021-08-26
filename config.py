"""
配置文件
"""


class Config:
    SECRET_KEY = 'MyHardPassword'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1/flasky"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '888888@cfiihz.com'
    MAIL_PASSWORD = '888888'
    FLASKY_MAIL_SUBJECT_PREFIX = '[flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <it@cfiihz.com>'
    FLASKY_ADMIN = 'yaoyuanfu@cfiihz.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TesttingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/flasky"


config = {
    'development': DevelopmentConfig,
    'testing': TesttingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
