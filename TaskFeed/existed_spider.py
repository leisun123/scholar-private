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
from TaskFeed.caee_utexas_task import CaeeUtexasTask
from TaskFeed.che_utexas_task import CheUtexasTask
from TaskFeed.cs_utexas_task import CSUtexasTask
from TaskFeed.ece_utexas_task import ECEUtexasTask
from TaskFeed.me_utexas_task import MeUtexasTask
from TaskFeed.tmi_utexas_task import TmiUtexasTask
from TaskFeed.eecs_berkeley_task import EECSBerkeleyTask
from TaskFeed.me_berkeley_task import MEBerkeleyTask
from TaskFeed.ce_berkeley_task import CEBerkeleyTask

EXISTED_SPIDER = [
    {
        'SpiderClass' : CaeeUtexasTask(),
        'Major' : 'Civil and Environmental Engineering',
        'Forecast' : 57
    },
    {
        'SpiderClass' : CheUtexasTask(),
        'Major' : 'Chemical Engineering',
        'Forecast' : 34
    },
    {
        'SpiderClass' : CSUtexasTask(),
        'Major' : 'Computer Science ',
        'Forecast' : 40
    },
    {
        'SpiderClass' : MeUtexasTask(),
        'Major' : 'MECHANICAL ENGINEERING',
        'Forecast' : 90
    },
    {
        'SpiderClass' : TmiUtexasTask(),
        'Major' : 'Materials Science and Engineering',
        'Forecast' : 100
    },
    
    {
        'SpiderClass' : ECEUtexasTask(),
        'Major' : 'Electrical and Computer Engineering',
        'Forecast' : 80
    },
    {
        'SpiderClass' : EECSBerkeleyTask(),
        'Major' : 'Electrical Engineering and Computer Sciences',
        'Forecast' : 130
    },
    {
        'SpiderClass': MEBerkeleyTask(),
        'Major' : 'Mechanical Engineering',
        'Forecast' : 53
    },
    {
        'SpiderClass' : CEBerkeleyTask(),
        'Major' : 'Civil and Environmental Engineering',
        'Forecast' : 52
    }

]