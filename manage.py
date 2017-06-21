#coding:utf-8
"""
@file:      manage
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/21 6:02
@description:
            --
"""
from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)