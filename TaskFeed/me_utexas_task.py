#coding:utf-8
"""
@file:      me_utexas_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 1:58
@description:
            --
"""
import random

import gevent

from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.me_utexas_rule import MAX_PAGE,BASE_URL
from utils.timer import Timer


class MeUtexasTask(Taskmanager):
    
    def __init__(self):
        #super(ScienceDirectTask,self).__init__()
        Taskmanager.__init__(self,"me_utexas")
        self.max_page = MAX_PAGE
        self.base_url = BASE_URL
    
    
    def run(self):
        all_greenlet = []
        all_greenlet.append(gevent.spawn(self._feed_page_queue,self.base_url))
        all_greenlet.append(gevent.spawn(self._item_loop))
        gevent.joinall(all_greenlet)
      
    def _feed_page_queue(self,base_url):
        for i in range(1,MAX_PAGE):
            page_url = base_url.format(i)
            self.info_queue.put(page_url)

            
    def _crawl_info(self,item_url):
        self.logger.info("processing info %s",item_url)
        from ScholarConfig.me_utexas_rule import RULES
        from CustomParser.me_utexas_parser import MeUtexasClass
        from lxml import etree
        html=fetch(item_url,proxies=None,logger=self.logger)
        sec=extract(RULES["item"],html,multi=True)
        for i in sec:
            MeUtexasClass(str(etree.tostring(i))).terminal_monitoring()
    
   
if __name__ == '__main__':
    s=MeUtexasTask()
    s.run()
    # from ScholarConfig.Rules import RULES
    # url = "http://europepmc.org/search?query=big+data&page=0"
    # html=fetch(url)
    # a=extract(RULES["item_url"],html)
    # print(a)