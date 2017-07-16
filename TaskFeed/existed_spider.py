#coding:utf-8
"""
@file:      existed_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 3:18
@description:
            --
"""
from .europepmc_task import EuropepmcTask

EXISTED_SPIDER = [
    {
        'SpiderClass' : EuropepmcTask,
        'BaseUrl' : 'http://www.sciencedirect.com'
    }
]