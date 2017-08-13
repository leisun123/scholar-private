#coding:utf-8
"""
@file:      cs_utexas
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/16 20:40
@description:
            --
"""
import gevent
from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from ScholarConfig.cs_utexas_rule import RULES,BASE_URL
from lxml import etree

class CSUtexasTask(Taskmanager):
    
    def __init__(self):
        #super(ScienceDirectTask,self).__init__()
        Taskmanager.__init__(self,"cs_utexas")
        self.base_url = BASE_URL
    
    def run(self):
        all_greenlet = []
        all_greenlet.append(gevent.spawn(self.crawl_info))
        all_greenlet.append(gevent.spawn(self._db_save_loop))
        gevent.joinall(all_greenlet)
        
    def crawl_info(self):
        from CustomParser.cs_utexas_parser import CSUtexasClass
        html = fetch(self.base_url,logger=self.logger)
        sec = extract(RULES["item"],html,multi=True)
        for i in sec:
            if i is not None:
                tmp = CSUtexasClass(str(etree.tostring(i)))
                parm = tmp.set_value()
                tmp.terminal_monitoring()
                self.parm_queue.put_nowait(parm)
        
   
if __name__ == '__main__':
    s=CSUtexasTask()
    s.run()
    # from ScholarConfig.Rules import RULES
    # url = "http://europepmc.org/search?query=big+data&page=0"
    # html=fetch(url)
    # a=extract(RULES["item_url"],html)
    # print(a)