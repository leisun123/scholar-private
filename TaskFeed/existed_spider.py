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
from CustomParser.ame_nd_parser import AmeNdTask
from SampleData import ame_nd, cse_nd ,ee_nd
from CustomParser.cse_nd_parser import CSENdTask
from CustomParser.ee_nd_parser import EENdTask
from CustomParser import cbe_udel_parser, me_udel_parser


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
        'SpiderClass' : AmeNdTask,
        'Major' : ame_nd.major,
        'Forecast' : None,
        'state' : False
    },
    {
        'SpiderClass' : CSENdTask,
        'Major' : cse_nd.major,
        'Forecast' : None,
        'state' : False,
        'error' : "504"
    },
    {
        'SpiderClass' : EENdTask,
        'Major' : ee_nd.major,
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
    }
    
]