#coding:utf-8
"""
@file:      __init__.py
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/21 4:11
@description:
            --
"""
from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    
    bootstrap.init_app(app)
    
    from .main import main
    app.register_blueprint(main)
    
    return app