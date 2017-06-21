#coding:utf-8
"""
@file:      __init__.py
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/21 4:22
@description:
            --
"""
from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,errors
