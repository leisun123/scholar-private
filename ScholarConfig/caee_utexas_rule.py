#coding:utf-8
"""
@file:      caeeutexas_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 5:00
@description:
            --
"""
RULES = {
    "item_url":"//div[@class='facdata']/h4/a/@href",
    "avatar":"//div[@class='facphoto']/img/@src",
    "name":"//h1/text()",
    "title_1":"//p[@class='depttitle']/text()",
    "title_2":"//p[@class='endowedtitle']/text()",
    "title_3":"//p[@class='society']/text()",
    "info":"//div[@class='facdata']/p",
    "keywords":"//*[@id='faccontent']/div[2]/p[1]/text()",
    "cooperation":"//*[@id='faccontent']/div[2]/p[3]/text()",
    "website":"//*[@id='faccontent']/div[2]/p[4]/a/@href"
}


BASE_URL =  "http://www.caee.utexas.edu"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20