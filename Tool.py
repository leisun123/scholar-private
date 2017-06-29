#coding:utf-8
"""
@file:      Tool
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2017/3/5 16:22
@description:
            --
"""
from lxml import etree
import requests
from Error import HTTPError,URLFetchError
import logging
from logger import logger
import time
from spider_config import USER_AGENT

proxy_manager=None

def fetch(url,timeout=10,from_web=True,retry_num=5):
    if not from_web:
        with open('','rb') as f:
            return f.read()
    else:
        kwargs={
            "headers": {
                "User-Agent": USER_AGENT,
                #"Referer": "http://www.douban.com/"
            },
        }
        kwargs["timeout"]=timeout
        resp=None
        for i in range(retry_num):
            try:
                #是否启动代理
                if proxy_manager is not None:
                    kwargs["proxies"]={
                        "http":proxy_manager.get_proxy()
                    }
                resp=requests.get(url,**kwargs)
                if resp.status_code!=200:
                    raise HTTPError(resp.status_code,url)
                break
            except Exception as exc:
                logger.warn("%s %d failed!\n%s",url,i,str(exc))
                time.sleep(2)
                continue
        if resp is None:
            raise URLFetchError(url)
        return resp.content.decode("UTF8")
    
def extract(regx,html_source,multi=False):
    #lxml解析
    if isinstance(html_source,str):
        html_source=etree.HTML(html_source)
    res=html_source.xpath(regx)
    if multi:
        return res
    return res[0] if res else None


def nameparser(name):
    from nameparser import HumanName
    first_name=HumanName(name)
    return first_name
    
if __name__ == '__main__':
    import re
    from spider_config import *
    # html=fetch("http://europepmc.org/abstract/MED/28480474")
    # emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
    # #print(html)
    # a=extract("//span[@class='author-refine-subtitle']/text()",html)
    # print(str(a))
    # email = re.search(emailRegex,str(a).replace(' ','')).group(0)
    # print(email)
    
    # html=fetch("http://europepmc.org/search?query=big%20data")
    # a=extract(RULES["item"],html,multi=True)
    # for i in a:
    #     b=i.split(';')[0]
    #     print(b)
    
    # html=fetch("http://europepmc.org/search?query=big%20data")
    # a=extract(RULES["item"],html)
    # print(a)
    
    # html=fetch("http://europepmc.org/abstract/MED/28609295")
    # #print(html)
    # a=extract(RULES["url"],html)
    # print(a)
    
    print(nameparser("Guobao liu").full_name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    