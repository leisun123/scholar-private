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
from CustomParser import    ame_nd_parser,\
                            cse_nd_parser,\
                            ee_nd_parser,\
                            cbe_udel_parser,\
                            me_udel_parser,\
                            ce_udel_parser

EXISTED_SPIDER = [
    {
        'SpiderClass' : CaeeUtexasTask(),
        'Major' : 'Civil and Environmental Engineering',
        'Forecast' : 57,
        'state' : True
    },
    {
        'SpiderClass' : CheUtexasTask(),
        'Major' : 'Chemical Engineering',
        'Forecast' : 34,
        'state' : True
    },
    {
        'SpiderClass' : CSUtexasTask(),
        'Major' : 'Computer Science ',
        'Forecast' : 40,
        'state' : True
    },
    {
        'SpiderClass' : MeUtexasTask(),
        'Major' : 'MECHANICAL ENGINEERING',
        'Forecast' : 90,
        'state' : True
    },
    {
        'SpiderClass' : TmiUtexasTask(),
        'Major' : 'Materials Science and Engineering',
        'Forecast' : 100,
        'state' : True
    },
    
    {
        'SpiderClass' : ECEUtexasTask(),
        'Major' : 'Electrical and Computer Engineering',
        'Forecast' : 80,
        'state' : True
    },
    {
        'SpiderClass' : EECSBerkeleyTask(),
        'Major' : 'Electrical Engineering and Computer Sciences',
        'Forecast' : 130,
        'state' : True
    },
    {
        'SpiderClass': MEBerkeleyTask(),
        'Major' : 'Mechanical Engineering',
        'Forecast' : 53,
        'state' : True
    },
    {
        'SpiderClass' : CEBerkeleyTask(),
        'Major' : 'Civil and Environmental Engineering',
        'Forecast' : 52,
        'state' : True
    },
    {
        'SpiderClass' : ame_nd_parser.AmeNdTask,
        'Major' : None,
        'Forecast' : None,
        'state' : False
    },
    {
        'SpiderClass' : cse_nd_parser.CSENdTask,
        'Major' : None,
        'Forecast' : None,
        'state' : False,
        'error' : "504"
    },
    {
        'SpiderClass' : ee_nd_parser.EENdTask,
        'Major' : None,
        'Forecast' : None,
        'state' : False
    },
    {
        'SpiderClass' : cbe_udel_parser.CBETask,
        'Major' : '',
        'Forecast' : None,
        'state' : False
    },
    {
        'SpiderClass' : me_udel_parser.MEUdelTask,
        'Major' : '',
        'Forecast' : None,
        'state' : False
    },
    {
        'SpiderClass' : ce_udel_parser.CEUdelTask,
        'Major' : '',
        'Forecast' : None,
        'state' : False
    }
]