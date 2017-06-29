from gevent import monkey
monkey.patch_all()
import gevent
from logger import logger
from Tool import extract
import random
from utils import Timer,ProxyManager
from spider_config import *
from ScholarParser import ScholarParser
from ScholarClass import Scholar
from Tool import fetch
import time

class ScholarManager(Scholar):
    def __init__(self,proxy_manager=None):
        super(ScholarManager, self).__init__()
        self.proxy_manager=proxy_manager

    def run(self):
        all_greenlet=[]
        # for entrance_url in self.entrance_url_list:
        #     timer=Timer(random.randint(0,2),self.interval)
        #     # greenlet=gevent.spawn(timer.run,self._init_page_tasks,entrance_url)
        #     # all_greenlet.append(greenlet)
        for i in range(1000):
            entrance_url="http://europepmc.org/search?query=big+data&page={}&sortby=Date%2BDESC".format(i)
            timer=Timer(random.randint(0,2),self.interval)
            greenlet=gevent.spawn(timer.run,self._init_page_tasks,entrance_url)
            all_greenlet.append(greenlet)
        all_greenlet.append(gevent.spawn(self._page_loop))
        all_greenlet.append(gevent.spawn(self._info_loop))
        gevent.joinall(all_greenlet)

    def reload_proxies(self):
        self.proxy_manager.reload_proxies()

    def _init_page_tasks(self,entrance_url):
         self.page_queue.put(entrance_url)

    def _page_loop(self):
        while 1:
            page_url=self.page_queue.get(block=True)
            gevent.sleep(4)
            self.pool.spawn(self._crawl_page,page_url)

    def _crawl_page(self,url):
        logger.info("processing page %s",url)
        html=fetch(url)
        #print(html.capitalize())
        item=extract(RULES["item_url"],html,multi=True)
        for i in item[1:]:
            temp=i.split(';')[0].replace('.','')
            self.info_queue.put("http://europepmc.org"+temp)

    def _info_loop(self):
        while 1:
            item_url=self.info_queue.get(block=True)
            gevent.sleep(4)
            self.pool.spawn(self._crawl_info,item_url)


    def _crawl_info(self,item_url):
        logger.info("processing info %s",item_url)

        from ScholarClass import Scholar
        scholar=Scholar()
        scholar.connectdb()
        sec=fetch(item_url)

        temp=ScholarParser(sec,scholar)
        temp.show_in_cmd()





if __name__ == '__main__':
    proxy_manager=ProxyManager("./proxy_list.txt",30)
    
    d=ScholarManager(proxy_manager)
    d.run()












