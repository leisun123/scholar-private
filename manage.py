#coding:utf-8
"""
@file:      manage
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-9 下午3:15
@description:
            --
"""

from BaseClass.common_task import CommonTask
from CustomParser.bio_nyu_parser import BIONyuClass
from CustomParser.ce_udel_parser import CEUdelClass
from SampleData.ce_udel import base_url,sample_url,data,item_url_rule
CEUdelTask = CommonTask(website_name=CEUdelClass.__name__,
               custom_parser=CEUdelClass,
               base_url=base_url,
               sample_url=sample_url,
               data=data,
               item_url_rule=item_url_rule,
               default_url="http://www.ce.udel.edu/directories/",
               is_url_joint=True
               )
CEUdelTask.run()

BIONyuTask = CommonTask(website_name=BIONyuClass.__name__,
               custom_parser=BIONyuClass,
               base_url=base_url,
               sample_url=sample_url,
               data=data,
               item_url_rule=item_url_rule,
               default_url="http://engineering.nyu.edu/",
               is_url_joint=True
               )
BIONyuTask.run()

