#coding:utf-8
"""
@file:      file_save_error
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/20 4:10
@description:
            --
"""
class FileSaveError(Exception):
    def __init__(self,path,file_name):
        self.path = path
        self.filename = file_name
        
    def __str__(self):
        return "{} save to {} failed!".format(self.path,self.filename)