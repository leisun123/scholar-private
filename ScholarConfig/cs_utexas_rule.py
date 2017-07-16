#coding:utf-8
"""
@file:      cs_utexas_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/16 17:50
@description:
            --
"""

RULES = {
    "avatar":"//div[@class='views-field-field_image']/img/@src",
    "item":"//div[contains(@class,'ds-2col faculty-block-fields clearfix')]",
    "keyword":"//div[@class='item-list']/ul/li/a/text()",
    "info":"//p[contains(@class,'margin-bottom-sm')]"
}


BASE_URL =  "https://www.cs.utexas.edu/faculty"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20
