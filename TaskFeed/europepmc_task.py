#coding:utf-8
"""
@file:      sc
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 3:12
@description:
            --
"""
import random

import gevent

from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.europepmc_rule import RULES,MAX_PAGE,BASE_URL
from utils.timer import Timer


class EuropepmcTask(Taskmanager):
    
    def __init__(self):
        #super(ScienceDirectTask,self).__init__()
        Taskmanager.__init__(self,"europepmc")
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
        for url in base_url:
            for i in range(MAX_PAGE):
                page_url = url.format(i)
                self.page_queue.put(page_url)

            
    def _feed_info_queue(self,url):
        self.logger.info("processing page %s",url)
        
        html=fetch(url,proxies=None,logger=self.logger)
        #print(html.capitalize())
        item=extract(RULES["item_url"],html,multi=True)
        for i in item[1:]:
            temp=i.split(';')[0].replace('.','')
            self.info_queue.put("http://europepmc.org"+temp)
    
    def _crawl_info(self,item_url):
        self.logger.info("processing info %s",item_url)
        from BaseClass.ThesisClass import ThesisInfo
        from CustomParser.europepmc_parser import ScienceDirect
        sec=fetch(item_url,proxies=None,logger=self.logger)
        ScienceDirect(sec).terminal_monitoring()
    
   
if __name__ == '__main__':
    s=EuropepmcTask()
    s.run()
    # from ScholarConfig.Rules import RULES
    # url = "http://europepmc.org/search?query=big+data&page=0"
    # html=fetch(url)
    # a=extract(RULES["item_url"],html)
    # print(a)