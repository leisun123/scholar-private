#coding:utf-8
"""
@file:      ce_berkeley_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 20:17
@description:
            --
"""
RULES = {
    "item_url":"//h4/a/@href",
    "avatar":"//*[@id='faculty-profile-summary-headshot']/img/@src",
    "name":"/html/body/div[2]/div/section/div/h1/text()",
    "title":"//*[@id='faculty-info-wrapper']/div[2]/div[1]/b/text()",
    "phone":"//b[text()='Phone']/../following-sibling::*/a/text()",
    "email":"//b[text()='Email']/../following-sibling::*/a/text()",
    "keywords":"//*[@id='faculty-info-wrapper']/div[2]/div[2]/i/text()",
    "website":"//b[text()='Website']/../following-sibling::*/a/text()",
    "bio":"//*[@id='faculty-research-biography']/p[2]/text()",
    "cooperation":"//*[@id='faculty-research-overview']/p[2]/text()"
}


BASE_URL =  "http://www.ce.berkeley.edu"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20

