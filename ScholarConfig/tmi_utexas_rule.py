#coding:utf-8
"""
@file:      tmi_utexas_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 12:04
@description:
            --
"""
RULES = {
    "item_url":"//td[@class='name']/a/@href",
    "avatar":"//img[@class='alignright']/@src",
    "name":"//h1[@class='page-title']/text()",
    "title":"//section[@class='entry-content clearfix']/span/h3/text()",
    "phone":"//section[@class='entry-content clearfix']/span/span[2]/text()",
    "email":"//section[@class='entry-content clearfix']/span/span[3]/a/text()",
    "website":"//section[@class='entry-content clearfix']/span/span[4]/a/text()",
    "keywords":"//section[@class='entry-content clearfix']/span/span[6]/a/text()",
    "cooperation":"//section[@class='entry-content clearfix']/span/span[7]/a/text()"
    
}


BASE_URL =  "http://tmi.utexas.edu/people/type/faculty/"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20