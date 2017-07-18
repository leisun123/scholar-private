#coding:utf-8
"""
@file:      tmi_utexas_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 12:13
@description:
            --
"""
import random

import gevent

from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.tmi_utexas_rule import RULES,BASE_URL
from utils.timer import Timer


class TmiUtexasTask(Taskmanager):
    
    def __init__(self):
        #super(ScienceDirectTask,self).__init__()
        Taskmanager.__init__(self,"tmi_utexas")
        self.base_url = BASE_URL
    
    
    def run(self):
        all_greenlet = []
        self.page_queue.put(BASE_URL)
        all_greenlet.append(gevent.spawn(self._page_loop))
        all_greenlet.append(gevent.spawn(self._item_loop))
        gevent.joinall(all_greenlet)
        
    def _feed_info_queue(self,url):
        self.logger.info("processing page %s",url)
        
        html=fetch(url,proxies=None,logger=self.logger)
        #print(html.capitalize())
        item=extract(RULES["item_url"],html,multi=True)
        for i in item:
            self.info_queue.put(i)
    
    def _crawl_info(self,item_url):
        self.logger.info("processing info %s",item_url)
        from BaseClass.ThesisClass import ThesisInfo
        from CustomParser.tmi_utexas_parser import TmiUtexasClass
        sec=fetch(item_url,proxies=None,logger=self.logger)
        TmiUtexasClass(sec).terminal_monitoring()
    
   
if __name__ == '__main__':
    s=TmiUtexasTask()
    s.run()
    # from ScholarConfig.Rules import RULES
    # url = "http://europepmc.org/search?query=big+data&page=0"
    # html=fetch(url)
    # a=extract(RULES["item_url"],html)
    # print(a)