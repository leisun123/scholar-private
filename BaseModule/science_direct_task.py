#coding:utf-8
"""
@file:      science_direct_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/17 1:13
@description:
            --
"""
import random
from multiprocessing import Pool as multi_pool
from gevent import monkey; monkey.patch_all()
import gevent
from gevent.pool import Pool as async_pool
from utils.connection import *
import queue
import requests
from utils.logger import get_logger
from BaseModule.science_direct_parser import ScienceDirectClass
from db.SqlHelper import SqlHelper
from utils.timer import Timer
from utils.proxy_manager import ProxyManager
from init import project_dir
from utils.selenuim_parser import SelenuimParser
from ScholarConfig.config import get_user_agent

major_list = {"Chemical":"http://www.sciencedirect.com/science/journals/sub/chemicaleng/all"}
class ScienceDirectTask(object):
    def __init__(self, use_proxy=True):
        self.journal_queue = queue.Queue()
        self.volume_queue = queue.Queue()
        self.thesis_queue = queue.Queue()
        self.parm_queue = queue.Queue()
        
        self.multi_pool = multi_pool()
        self.async_pool = async_pool(size=50)
        
        self.requests_session = requests.session()
        
        self.use_proxy = use_proxy
        self.timer = Timer(start=random.randint(0,5), interval=30)
        
        #重载代理
        self.timer.run(self.reload_proxies())

        self.logging = None
        self.proxy_manager = None
        self.driver = None
        
    def reload_proxies(self):
        self.proxy_manager.reload_proxies()
        
    def refresh_webdriver(self):
        if self.use_proxy is not False:
            self.use_proxy =  self.timer.run(self.proxy_manager.get_proxy)
        user_agent = self.timer.run(get_user_agent())
        self.driver  = SelenuimParser(self.proxy_manager, user_agent=user_agent,
                      user_proxy=self.use_proxy)
        
        
    def MainTask(self):

        # for subject,subject_url in major_list.items():
        #     self.multi_pool.apply_async(self._feed_journal_loop, args=(subject, subject_url))
        # self.multi_pool.close()
        # self.multi_pool.join()
        self._feed_journal_loop("Chemical",
                                "http://www.sciencedirect.com/science/journals/sub/chemicaleng/all")
        
    def _feed_journal_loop(self, subject, subject_url):
        
        self.logging = get_logger(name=subject)
        self.proxy_manager = ProxyManager("{}/1.txt".format(project_dir), self.logging)
        
        self.logging.info("Processing journal {}".format(subject_url))
        html_source = fetch(subject_url, requests_session=self.requests_session)
        
        journal_item = iter(extract("//li[@class='browseimpBrowseRow']/ul/li/span/a/@href", html_source, multi=True))
        try:
            while True:
                self.journal_queue.put_nowait('http://www.sciencedirect.com{}'.\
                                     format(next(journal_item)))
        except StopIteration:
            self.logging.info("Journal_Queue Get {} seeds".format(self.journal_queue._qsize()))
        
        #self._run()
        
        
    def _run(self):
        all_greenlet = []
        all_greenlet.append(gevent.spawn(self._refresh_webdriver))
        all_greenlet.append(self._journal_loop())
        all_greenlet.append(self._volume_loop())
        all_greenlet.append(self._thesis_loop())
        all_greenlet.append(self._parm_loop())
        gevent.joinall(all_greenlet)
        
    
    def _journal_loop(self):
        while True:
            subject_url = self.journal_queue.get(block=True)
            gevent.sleep(2)
            self.async_pool.spawn(self._feed_volume_queue, subject_url)
    
    
    def _feed_volume_queue(self, subject_url):
        
        html_source = fetch(subject_url, requests_session=self.requests_session)
        volume_item = iter(extract("//div[@id='volumeIssueData']/li/a[@class='cLink volLink']/@href", html_source, multi=True))
        
        try:
            while True:
                tmp = next(volume_item)
                #parse 2000 year later
                if int(tmp.split(' ')[-1]) > 2000:
                    self.volume_queue.put_nowait('{}{}'.format(subject_url, tmp))
        except StopIteration:
            self.logging.info("Volume_Queue Get {} seeds".format(self.volume_queue._qsize()))
            
        
    def _volume_loop(self):
        
        while True:
            volume_url = self.volume_queue.get(block=True)
            gevent.sleep(2)
            self.async_pool.spawn(self._feed_thesis_queue, volume_url)
            
    def _feed_thesis_queue(self, volume_url):
        
        html_source = fetch(volume_url, requests_session=self.requests_session)
        thesis_item = iter(extract("//li[@class='title oaBlock']/h4/a/@href", html_source, multi=True))
        
        try:
            while True:
                self.thesis_queue.put_nowait(next(thesis_item))
        except StopIteration:
            self.logging.info("Thesis_Queue Get {} seeds".format(self.thesis_queue._qsize()))
    
    def _thesis_loop(self):
        
        while True:
            thesis_url = self.thesis_queue.get(block=True)
            gevent.sleep(2)
            self.async_pool.spawn(self._feed_parm_queue, thesis_url)
    
    def _feed_parm_queue(self, thesis_url):
        
        tmp = ScienceDirectClass(sec=thesis_url, webdriver=self.driver)
        tmp._parser_data()
        parm = tmp.set_value()
        self.parm_queue.put_nowait(parm)
    
    def _parm_loop(self):
        
        while True:
            parm = self.parm_queue.get(block=True)
            gevent.sleep(10)
            self.async_pool.spawn(self._feed_db, **parm)
            
    def _feed_db(self, **parm):
        
        sqlhepler = SqlHelper(logger=self.logging)
        sqlhepler.insert_scholar(**parm)
        
if __name__ == '__main__':
    # html_source = fetch("http://www.sciencedirect.com/science/journal/22126708?sdc=1", requests_session=requests.session())
    # volume_item = iter(extract("//li[@class='title oaBlock']/h4/a/@href", html_source, multi=True))
    # while True:
    #     i = next(volume_item)
    #     print(i)
    s = ScienceDirectTask(use_proxy=False)
    s.MainTask()
        
        
        
        
        