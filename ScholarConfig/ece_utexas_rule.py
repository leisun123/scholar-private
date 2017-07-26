#coding:utf-8
"""
@file:      ece_utexas_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 7:40
@description:
            --
"""
RULES = {
    "item_url":"//table[@class='views-view-grid cols-7']/tbody/tr/td/div/div[@class='field-content']/a/@href",
    "avatar":"//*[@id='faculty-profile-panel']/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/figure/a/img/@src",
    "name":"//*[@id='faculty-profile-panel']/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/h1/text()",
    "title":"//*[@id='faculty-profile-panel']/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div/div/div/text()",
    "phone":"//*[@id='faculty-profile-panel']/div/div[3]/div/div/div/div[3]/div/div/section/div/div/text()",
    "email-1":"//*[@id='faculty-profile-panel']/div/div[3]/div/div/div/div[5]/div/div/section/div/div/a/text()",
    "email-2":"//*[@id='faculty-profile-panel']/div/div[3]/div/div/div/div[3]/div/div/section/div/div/a/text()",
    "keywords":"//*[@id='faculty-profile-panel']/div/div[2]/div/div[3]/div/div[1]/div/div/div/div/section/div/div/a/text()",
    "website-1":"//*[@id='faculty-profile-panel']/div/div[3]/div/div/div/div[9]/div/div/div/div/div/a/@href",
    "website-2":"//*[@id='faculty-profile-panel']/div/div[3]/div/div/div/div[5]/div/div/div/div/div/a/@href",
    "bio":"//*[@id='faculty-profile-panel']/div/div[2]/div/div[2]/div/div/div/div/div/div/p[1]/text()",
    "cooperation":"//*[@id='faculty-profile-panel']/div/div[2]/div/div[3]/div/div[2]/div/div/div/div/section/div/div/text()"
}

BASE_URL =  "http://www.ece.utexas.edu"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20
