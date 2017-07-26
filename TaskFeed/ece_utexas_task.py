#coding:utf-8
"""
@file:      ece_utexas_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 7:41
@description:
            --
"""

import gevent
from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.ece_utexas_rule import RULES,BASE_URL

class ECEUtexasTask(Taskmanager):
    
    def __init__(self):
        Taskmanager.__init__(self,"eceutexastask")
        self.base_url = BASE_URL
    
    
    def run(self):
        all_greenlet = []
        self.page_queue.put_nowait("http://www.ece.utexas.edu/people")
        all_greenlet.append(gevent.spawn(self._page_loop))
        all_greenlet.append(gevent.spawn(self._item_loop))
        all_greenlet.append(gevent.spawn(self._db_save_loop))
        gevent.joinall(all_greenlet)
      
        
    def _feed_info_queue(self,url):
        self.logger.info("processing page %s",url)
        
        html=fetch(url,proxies=None,logger=self.logger)
        #print(html.capitalize())
        item=extract(RULES["item_url"],html,multi=True)
        for i in item[:88]:
            self.info_queue.put_nowait(BASE_URL + i)
    
    def _crawl_info(self,item_url):
        self.logger.info("processing info %s",item_url)
        from CustomParser.ece_utexas_parser import ECEUtexasClass
        sec=fetch(item_url,proxies=None,logger=self.logger)
        tmp = ECEUtexasClass(sec)
        parm = tmp.set_value()
        tmp.terminal_monitoring()
        self.parm_queue.put_nowait(parm)
        
   
if __name__ == '__main__':
    s=ECEUtexasTask()
    s.run()