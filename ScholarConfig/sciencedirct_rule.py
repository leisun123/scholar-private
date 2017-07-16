#coding:utf-8
"""
@file:      sciencedirct_task
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/14 18:02
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
    "item_url":"//a[@class='cLink artTitle S_C_artTitle ']/@href",
    "title":"//h1[@class='svTitle']/text()",
    "author":"//a[@class='authorName svAuthor']/text()",
    "url": "//a[@id='pdfLink']/@href",
    "email":"//a[@class='auth_mail']/@href"
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
