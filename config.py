#coding:utf-8
"""
@file:      config,py
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/29 23:15
@description:
            --
"""
DB_CONFIG={

    'DB_CONNECT_TYPE':'sqlalchemy',#'pymongo'sqlalchemy
    # 'DB_CONNECT_STRING':'mongodb://localhost:27017/'
    'DB_CONNECT_STRING':'sqlite:///'+os.path.dirname(__file__)+'/data/proxy.db'
    #DB_CONNECT_STRING = 'mysql+mysqldb://root:root@localhost/proxy?charset=utf8'
}