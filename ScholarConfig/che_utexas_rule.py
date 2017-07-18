#coding:utf-8
"""
@file:      che_utexas
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/18 14:14
@description:
            --
"""
RULES = {
    "item_url":"//table/tbody/tr/td[2]/a/@href",
    "avatar":"//img[contains(@class,'alignright')]/@src",
    "name":"//h2[@class='page-title']/text()",
    "title":"//*[@class='post']/div/h4[1]/text()",
    "phone":"//*[@class='post']/div/table/tbody/tr[2]/td[2]/text()",
    "email":"//*[@class='post']/div/table/tbody/tr[4]/td[2]",
    "keywords":"//*[@class='post']/div/h4[2]/a/text()",
    "cooperation":"//*[@class='post']/div/p[5]/text()",
    "bio":"//*[@class='post']/div/p[6]"

}


BASE_URL =  "http://che.utexas.edu/faculty-staff/faculty-directory/"

#抓取前多少页
#MAX_PAGE = 30
# 并发数
CRWAL_POOL_SIZE = 20