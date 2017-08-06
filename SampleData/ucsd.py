#coding:utf-8
"""
@file:      be_ucsd
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-7 上午12:41
@description:
            --
"""
#学者列表入口
base_url = 'http://jacobsschool.ucsd.edu/faculty/faculty_bios/'
#特征训练示例学者入口
sample_url = 'http://jacobsschool.ucsd.edu/faculty/faculty_bios/index.sfe?fmp_recid=23'
#条目链接
item_url_rule = "//td/p/a/@href"

#填补缺失
bio_rule = "//strong[1]"
phone_rule = "//strong[text()='Office Phone:']/.."
avatar_rule = "//img[@width='120']/@src"
website_rule = "//a[text()='Web Page']/@href"



#示例数据
data = {#"avatar":"https://engineering.nd.edu/profiles/hfernando/@@images/fbd01446-37e5-43c7-8f8c-de8ff322f962.jpeg",
        "name":"Anthony S. Acampora",
        "title":"Prof Emeritus",
        #"phone":"858-534-5438",
        "email":"aacampora@ucsd.edu",
        #"website":"",
        "cooperation":"California Institute for Telecommunications and Information Technology",
        "keywords":"Center for Wireless Communications",
        "major":"Electrical and Computer Engineering"
        }

#组织名
organization = "UC San Diego Jacobs School of Engineering"

#主修专业


# from utils.connection import *
# html = fetch(sample_url)
# #print(html)
# a = extract(phone_rule, html)
# print(a.xpath('string(.)'))