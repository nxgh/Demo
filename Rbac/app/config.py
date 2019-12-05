# -*- coding: utf-8 -*-

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGO_URI = 'mongodb://rbac:password@localhost:20017/rbac'  


class TestingConfig(BaseConfig):
    TESTING = True
    MONGO_URI = 'mongodb://blog_test:password@localhost:27017/blog_test'  

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = \
        MONGO_URI = 'mongodb://blog_test:password@localhost:27017/blog_test'  

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
