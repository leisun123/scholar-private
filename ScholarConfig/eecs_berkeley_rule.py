#coding:utf-8
"""
@file:      eecs_berkeley_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 18:28
@description:
            --
"""
RULES = {
    "item_url":"//div[@class='media-body']/h3/a/@href",
    "avatar":"//*[@id='page']/main/div/div[2]/article/img/@src",
    "name":"//h1[@class='fn']/text()",
    "title":"//*[@id='page']/main/div/div[2]/article/div/header/p/text()",
    "phone":"//*[@id='page']/main/div/div[2]/aside/section[2]/p[2]/a/text()",
    "email-1":"//*[@id='page']/main/div/div[2]/aside/section[2]/div/a/text()",
    "email-2":"//*[@id='page']/main/div/div[2]/aside/section[4]/p/a[2]/text()",
    "keywords":"//*[@id='page']/main/div/div[2]/article/div/section[1]/div[1]/ul[@class='Research Areas']/li/a/text()",
    "website":"//*[@id='page']/main/div/div[2]/aside/section[1]/ul/li[1]/a/@href",
    "bio":"//*[@id='page']/main/div/div[2]/article/div/section[2]/div/text()",
    "cooperation":"//*[@id='page']/main/div/div[2]/article/div/section[1]/div[2]/ul[@class='Research Areas']/li/a/text()"
}

BASE_URL =  "https://www2.eecs.berkeley.edu"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20