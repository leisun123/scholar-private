#coding:utf-8
"""
@file:      sciencedirect_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/14 17:51
@description:
            --
"""
import random

import gevent

from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.europepmc_rule import RULES,MAX_PAGE,BASE_URL
from utils.timer import Timer

class ScienceDirect(Taskmanager):
    
    def __init__(self):
        Taskmanager.__init__(self,"sciencedirct")
        self.max_page = MAX_PAGE
        self.base_url = BASE_URL
        
    def run(self):
        all_greenlet = []
        all_greenlet.append(gevent.spawn(self._feed_page_queue,self.base_url))
        all_greenlet.append(gevent.spawn(self._page_loop))
        all_greenlet.append(gevent.spawn(self._item_loop))
        proxy_timer = Timer(random.randint(10*60,20*60),random.randint(10*60,20*60))
        all_greenlet.append(gevent.spawn(proxy_timer.run(self.proxy_manager.reload_proxies)))
        gevent.joinall(all_greenlet)
        
    def _feed_page_queue(self,base_url):
        pass