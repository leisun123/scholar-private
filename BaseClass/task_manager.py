#coding:utf-8
"""
@file:      task_manager
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 1:22
@description:
            --
"""
from gevent import monkey

from utils.logger import get_logger

monkey.patch_all()

import gevent

from gevent.pool import Pool
from gevent.queue import Queue
from db.SqlHelper import SqlHelper
from ScholarConfig.config import CRWAL_POOL_SIZE
from utils.proxy_manager import ProxyManager
class Taskmanager(object):
    
    def __init__(self,logging_name):
        
        #self.interval = WATCH_INTERVAL
        self.crawl_pool = Pool(size=CRWAL_POOL_SIZE)
        self.logger = get_logger(logging_name)
        self.page_queue = Queue()
        self.info_queue = Queue()
        self.parm_queue = Queue()
        self.proxy_manager = ProxyManager("../utils/1.txt",self.logger)
        #self.timer = Timer(random.randint(0,2),self.interval)
        self.proxys = self.proxy_manager.get_proxy()
        self.count = 0
        
    def run(self):
        pass
    
    def reload_proxies(self):
        self.proxy_manager.reload_proxies()
        
    def _feed_page_queue(self,base_url):
        pass
    
    def _page_loop(self):
        while 1:
            page_url=self.page_queue.get(block=True)
            gevent.sleep(1)
            self.crawl_pool.spawn(self._feed_info_queue,page_url)
    
    def _feed_info_queue(self,url):
        pass
    
    def _item_loop(self):
        while 1:
            item_url=self.info_queue.get(block=True)
            gevent.sleep(1)
            self.crawl_pool.spawn(self._crawl_info,item_url)
            
    def _crawl_info(self,item_url):
        pass
    
    def _db_save_loop(self):
        while 1:
            parm = self.parm_queue.get(block=True)
            self.count = self.count+1
            self.crawl_pool.spawn(SqlHelper(logger=self.logger).insert_scholar,**parm)
            
        
    

    
    
    