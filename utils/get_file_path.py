#coding:utf-8
"""
@file:      get_file_path
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/31 14:08
@description:
            --
"""
import os
def current_file_name(path):
    tmp = os.path.realpath(os.path.join(path, '..')).split('\\')
    return tmp[len(tmp)-1][0:-3]