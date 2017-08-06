#coding:utf-8
"""
@file:      common_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/1 2:05
@description:
            --
"""
import gevent
from BaseClass.task_manager import Taskmanager
from utils.connection import fetch,extract
from utils.auto_generate import auto_generate

class CommonTask(Taskmanager):
    
    def __init__(self,website_name,
                      custom_parser,
                      base_url,
                      sample_url,
                      data,
                      item_url_rule,
                      default_url=None,
                      is_url_joint = False):
        Taskmanager.__init__(self,website_name)
        self.website_name = website_name
        self.custom_parser = custom_parser
        self.base_url = base_url
        self.sample_url = sample_url
        self.data = data
        self.item_url_rule = item_url_rule
        self.default_url = default_url
        self.is_url_joint = is_url_joint
        
    def run(self):
        all_greenlet = []
        self.page_queue.put_nowait(self.base_url)
        all_greenlet.append(gevent.spawn(self._page_loop))
        all_greenlet.append(gevent.spawn(self._item_loop))
        all_greenlet.append(gevent.spawn(self._db_save_loop))
        gevent.joinall(all_greenlet)
      
        
    def _feed_info_queue(self,url):
        self.logger.info("processing page %s",url)
        
        html = fetch(url,proxies=None,logger=self.logger)
        #print(html.capitalize())
        item = extract(self.item_url_rule, html, multi=True)
        if not self.is_url_joint:
            for i in item:
                self.info_queue.put_nowait(i)
        else:
            for i in item:
                self.info_queue.put_nowait(self.default_url + i)
    
    def _crawl_info(self,item_url):
        self.logger.info("processing info %s",item_url)
        
        self.parse_data = auto_generate( sampleurl=self.sample_url,
                                         data=self.data,
                                         common_url=item_url)
        
        sec=fetch(item_url, proxies=None, logger=self.logger)
        tmp = self.custom_parser(sec,self.parse_data)
        parm = tmp.set_value()
        tmp.terminal_monitoring()
        self.parm_queue.put_nowait(parm)
        
if __name__ == '__main__':
    from SampleData.ame_nd import base_url,sample_url,data,item_url_rule
    from CustomParser.ame_nd_parser import AmeNdClass
    a = CommonTask(website_name=AmeNdClass.__name__,
                   custom_parser=AmeNdClass,
                   base_url=base_url,
                   sample_url=sample_url,
                   data=data,
                   item_url_rule=item_url_rule
                   )
    a.run()