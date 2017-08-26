#coding:utf-8
"""
@file:      me_berkeley_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 19:10
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

import gevent
from BaseModule.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.me_berkeley_rule import RULES,BASE_URL

class MEBerkeleyTask(Taskmanager):
    
    def __init__(self):
        Taskmanager.__init__(self,"eecsberkeleytask")
        self.base_url = BASE_URL
    
    
    def run(self):
        all_greenlet = []
        self.page_queue.put_nowait("http://www.me.berkeley.edu/people/faculty")
        all_greenlet.append(gevent.spawn(self._page_loop))
        all_greenlet.append(gevent.spawn(self._item_loop))
        all_greenlet.append(gevent.spawn(self._db_save_loop))
        gevent.joinall(all_greenlet)
      
        
    def _feed_info_queue(self,url):
        self.logger.info("processing page %s",url)
        
        html=fetch(url,proxies=None,logger=self.logger)
        #print(html.capitalize())
        item=extract(RULES["item_url"],html,multi=True)
        for i in item:
            self.info_queue.put_nowait(BASE_URL + i)
    
    def _crawl_info(self,item_url):
        self.logger.info("processing info %s",item_url)
        from CustomParser.me_berkeley_parser import MEBerkeleyClass
        sec=fetch(item_url,proxies=None,logger=self.logger)
        tmp = MEBerkeleyClass(sec)
        parm = tmp.set_value()
        tmp.terminal_monitoring()
        self.parm_queue.put_nowait(parm)
        
   
if __name__ == '__main__':
    s=MEBerkeleyTask()
    s.run()