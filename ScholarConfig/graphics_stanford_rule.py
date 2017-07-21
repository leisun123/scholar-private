#coding:utf-8
"""
@file:      graphics_stanford_rule
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/20 15:50
@description:
            --
"""
#coding:utf-8
RULES = {
    "item_url":"//h3[contains(@class,'description')]/a/@href",
    "avatar":"//*[contains(@class,'banner profile')]/div/div/div/div/div[1]/img/@src",
    "name":"//div[contains(@class,'nameAndTitle')]/h1/text()",
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