#coding:utf-8
"""
@file:      Rules
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 5:42
@description:
            --
"""
keywords = ["big data",
            "data analyse",
            "cluster analysis",
            "data clustering",
            "data mining",
            "data visualization",
            "data statistics",
            "machine learning",
            "deep learning",
            "database",
            "cloud computing",
            "distributed computation",
            "distributed memory",
            ]


RULES = {
    "item_url":"//div[@itemprop='item']/a[@class='resultLink']/@href",
    "title":"//span[@class='abs_citation_title']/text()",
    "source_url":"//meta[@name='citation_abstract_html_url']/@content",
    "keywords":"",
    "publish_time":"//span[@class='abs_nonlink_metadata cye-lm-tag']/text()",
    "abstract":"//div[@id='abstract_text_plain']/text()",
    "type":"//div[@class='abs_nonlink_metadata cye-lm-tag']/text()",
    "doi":"//span[@class='cye-lm-tag']/a/text()",
    "scholar_info_list":"//div[@class='inline-block']",
    "author_name":"//span[contains(@class,'abstract--author-name')]/text()",
    "affiliation":"//span[contains(@class,'author-refine-subtitle')]/@title"
}

MAX_PAGE = 5

BASE_URL =  ["http://europepmc.org/search?query=big+data&page={}",
             "http://europepmc.org/search?query=data analyse&page={}",
             "http://europepmc.org/search?query=cluster analysis&page={}",
             "http://europepmc.org/search?query=data clustering&page={}",
             "http://europepmc.org/search?query=data mining&page={}",
             "http://europepmc.org/search?query=data visualization&page={}",
             "http://europepmc.org/search?query=data statistics&page={}",
             "http://europepmc.org/search?query=machine learning&page={}",
             "http://europepmc.org/search?query=deep learning&page={}",
             "http://europepmc.org/search?query=database&page={}",
             "http://europepmc.org/search?query=cloud computing&page={}",
             "http://europepmc.org/search?query=distributed computation&page={}",
             "http://europepmc.org/search?query=distributed memory&page={}"
             ]

#抓取前多少页
MAX_PAGE = 30

# 并发数
CRWAL_POOL_SIZE = 5