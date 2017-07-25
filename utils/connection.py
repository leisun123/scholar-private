#coding:utf-8
"""
@file:      dom_build
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/30 3:13
@description:
            --
"""
import time

import requests
from lxml import etree

from ScholarConfig.config import proxies
from ErrorHandle.request_error import HTTPError, URLFetchError
from ScholarConfig.config import USER_AGENT
from utils.selenuim_parse import SelenuimParse


def fetch(url,timeout=10,from_web=True,retry_num=5,proxies=None,logger=None,decode=True):
    if not from_web:
        with open('','rb') as f:
            return f.read()
    else:
        kwargs={
            "headers": {
                "User-Agent": USER_AGENT,
            }
        }
        kwargs["timeout"]=timeout
        resp=None
        for i in range(retry_num):
            try:
                #是否启动代理
                if proxies is not None:
                    kwargs["proxies"] = { "http": proxies,\
                                          "https": proxies, }
                resp=requests.get(url,**kwargs)
                if resp.status_code != 200:
                    raise HTTPError(resp.status_code,url)
                break
            except Exception as exc:
                logger.warn("%s %d failed!\n%s",url,i,str(exc))
                time.sleep(2)
                continue
        if resp is None:
            raise URLFetchError(url)
        if decode:
            return resp.content.decode("UTF8")
        else:
            return resp.content
        
def extract(regx,html_source,multi=False):
    #lxml解析
    if isinstance(html_source,str):
        html_source=etree.HTML(html_source)
    res=html_source.xpath(regx)
    if multi:
        return res
    return res[0] if res else None

    
if __name__ == '__main__':
    from ScholarConfig.europepmc_rule import *
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
    
    # html=fetch('http://www.sciencedirect.com/science/article/pii/S0020025515006581')
    # print(html)
    
        # html = fetch('http://europepmc.org/abstract/MED/28140776')
        # tmp = extract(RULES['scholar_info_list'],html,multi=True)
        #
        # # for i in tmp[1:]:
        # #     print(111111111111111111111111111111111111111111111111111111111111111)
        # #     print(etree.tostring(i))
        # b=[]
        # for i in tmp:
        #     name=extract(RULES["author_name"],str(etree.tostring(i)))
        #     affiliation=extract(RULES["affiliation"],str(etree.tostring(i)))
        #     emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
        #     import re
        #     a=re.search(emailRegex,str(affiliation).replace(' ',''))
        #     if a is not None:
        #         email=a.group(0)
        #     else:
        #         email=None
        #     if affiliation is not None:
        #         m=affiliation.split(',')
        #         profession=m[0]
        #         university=m[1]
        #         city=m[2]
        #         country=m[3]
        #     else:
        #         profession=None
        #         university=None
        #         city=None
        #         country=None
        #     b.append({"name":name,"email":email,"profession":profession,"university":university,"city":city,"country":country})
        #
        # for i in b:
        #     print(i["name"])
    RULES = {
    "item_url":"//a[@class='cLink artTitle S_C_artTitle ']/@href",
    "title":"//h1[@class='svTitle']/text()",
    "source_url":"//link[@rel='canonical']/@href",
    "keywords":"//div[@class='keyword']/span[@class='cye-lm-tag']/text()",
    "publish_time":"//span[@class='cye-lm-tag']/text()",
    "abstract":"//p[@class='cye-lm-tag']/text()",
    "doi":"//a[@class='doi']/text()",
    "author":"//a[@class='authorName svAuthor']/text()",
    "pdf_url":"//a[@class='download-link']/@href",
    "email":"//a[@class='auth_mail']/@href",
    "scholar_info_list_1":"//a[@class='']",
    "scholar_info_list_2":"//dl[@class='affiliation']/dd/text()",
}
    html=SelenuimParse("http://www.sciencedirect.com/science/article/pii/S1570870516301627")
    from bs4 import BeautifulSoup
    #print(html)
    title=extract(RULES["title"],html)
    source_url=extract(RULES["source_url"],html)
    keywords=extract(RULES["keywords"],html,multi=True)
    publish_time=extract(RULES["publish_time"],html)
    abstract=extract(RULES["abstract"],html)
    type = None
    doi = extract(RULES("doi"),html)
    pdf_url = "http://www.sciencedirect.com{}".format(extract(RULES["pdf_url"],html))
    print(title,source_url,publish_time,abstract,doi,pdf_url)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    