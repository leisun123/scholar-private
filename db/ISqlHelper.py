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
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

class ISqlHelper(object):
    
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
    
