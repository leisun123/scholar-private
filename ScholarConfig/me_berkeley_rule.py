#coding:utf-8
"""
@file:      me_berkeley_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 19:10
@description:
            --
"""
RULES = {
    "item_url":"//a[@class='anchor-handle']/@href",
    "avatar":"//*[@id='content']/article/div[1]/div/div/img/@src",
    "name":"//*[@id='content']/article/h2/a/text()",
    "title":"//*[@id='content']/article/div[2]/div/div/text()",
}

BASE_URL =  "http://www.me.berkeley.edu"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20