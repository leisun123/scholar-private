#coding:utf-8
"""
@file:      parse_error
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 2:57
@description:
            --
"""

def except_return_none(func,ModelName):
    def wrapper(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            print('{}:\n\tError in {}(): {}'\
                  .format(ModelName,func.__name__,str(e)))
            return None
    return wrapper


#尽量用有返回值的
def except_pass(func,ModelName):
    def wrapper(*args, **kwargs):
        try:
            func(*args,**kwargs)
        except Exception as e:
            print('{}:\n\tError in {}(): {}'\
                  .format(ModelName,func.__name__,str(e)))
    return wrapper
