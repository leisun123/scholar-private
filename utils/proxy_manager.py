#coding:utf-8
"""
@file:      proxymanager
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 18:29
@description:
            --
"""
import random
import time

class ProxyManager(object):
    """
    代理管理器
    """
    def __init__(self,proxies_or_path,logging,interval_per_ip=0,is_single=False):
        '''
        @proxies_or_path, basestring or list, 代理path或列表
        @interval_per_ip, int, 每个ip调用最小间隔
        @is_single, bool, 是否启用单点代理,例如使用squid
        '''
        self.proxies_or_path = proxies_or_path
        self.host_time_map = {}
        self.interval = interval_per_ip
        self.is_single = is_single
        self.init_proxies(self.proxies_or_path)
        self.logging = logging
        
    def init_proxies(self,proxies_or_path):
        if isinstance(proxies_or_path,str):
            if self.is_single:
                self.proxies = proxies_or_path
            else:
                with open(proxies_or_path) as f:
                    self.proxies = f.readlines()
        else:
            self.proxies = proxies_or_path
            
    def reload_proxies(self):
        if not isinstance(self.proxied_or_path,str):
            raise TypeError("proxies_or_path ")
        if self.is_single:
            raise TypeError("is_single must be False!")
        with open(self.proxies_or_path) as f:
            self.proxies = f.readlines()
        self.logging.info("reload %s proxies ...",len(self.proxies))
        
    def get_proxy(self):
        '''
        获取一个可用代理
        :return:
        '''
        if self.is_single:
            return self.proxies
        proxy = self.proxies[random.randint(0,len(self.proxies)-1)].strip()
        host,_ = proxy.split(':')
        lastest_time = self.host_time_map.get(host,0)
        interval = time.time() - lastest_time
        if interval < self.interval:
            self.logging.info("%s waiting",proxy)
            time.sleep(self.interval)
        self.host_time_map[host] = time.time()
        return "http://%s" % proxy.strip()
        
if __name__ == '__main__':
            from utils.connection import fetch
            from utils.logger import get_logger
            logger=get_logger("ScienceDirectTask")
            p = ProxyManager("./1.txt",logger)
            a=p.get_proxy()
            b=fetch(url="http://icanhazip.com",proxies=a,logger=logger)
            print(b)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        