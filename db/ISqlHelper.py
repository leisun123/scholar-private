#coding:utf-8
"""
@file:      ISqlHelper
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/29 23:18
@description:
            --
"""
#coding:utf-8

class ISqlHelper(object):
    params = {'ip':None,'port':None,'types':None,'protocol':None,'country':None,'area':None}
    def init_db(self):
        raise NotImplemented
    def drop_db(self):
        raise NotImplemented

    def insert(self,value=None):
        raise NotImplemented

    def delete(self, conditions=None):
        raise NotImplemented
    def update(self, conditions=None,value=None):
        raise NotImplemented
    def select(self, count=None,conditions=None):
        raise NotImplemented