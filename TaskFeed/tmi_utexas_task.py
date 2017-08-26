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
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

import gevent

from BaseModule.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.tmi_utexas_rule import RULES,BASE_URL

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
        from BaseModule.ThesisClass import ThesisInfo
        from CustomParser.tmi_utexas_parser import TmiUtexasClass
        sec=fetch(item_url,proxies=None,logger=self.logger)
        tmp = TmiUtexasClass(sec)
        parm = tmp.set_value()
        tmp.terminal_monitoring()
        self.parm_queue.put_nowait(parm)
    
   
if __name__ == '__main__':
    s=TmiUtexasTask()
    s.run()
    # from ScholarConfig.Rules import RULES
    # url = "http://europepmc.org/search?query=big+data&page=0"
    # html=fetch(url)
    # a=extract(RULES["item_url"],html)
    # print(a)