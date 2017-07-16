#coding:utf-8
"""
@file:      me_utexas_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 2:07
@description:
            --
"""
RULES = {
    "item":"//div[contains(@class,'facentry')]",
    "avatar":"//div[@class='facphoto']/img/@src",
    "name":"//div[@class='facdata']/h3/a/text()",
    "title_1":"//p[@class='depttitle']/text()",
    "title_2":"//p[@class='endowedtitle']/text()",
    "title_3":"//p[@class='society']/text()",
    "email":"//p/a/text()",
    "info":"//div[@class='facdata']/p"
}


BASE_URL =  "http://me.utexas.edu/faculty/faculty-directory/page/{}"

#抓取前多少页
MAX_PAGE = 9
# 并发数
CRWAL_POOL_SIZE = 20
