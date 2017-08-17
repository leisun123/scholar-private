#coding:utf-8
"""
@file:      mccormick_northwestern
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-13 下午9:37
@description:
            --
"""

#学者列表入口
base_url = 'http://www.mccormick.northwestern.edu/mechanical/people/faculty/'
#特征训练示例学者入口
sample_url = 'http://www.mccormick.northwestern.edu/research-faculty/directory/profiles/chen-wei.html'
#条目链接
item_url_rule = "//h3/a/@href"
avatar_rule = "//div/img/@src"
website_rule = "//a[text()='Website']/@href"
email_rule = "//a[@class='mail_link']/@href"
name_rule = "//h1[@id='page-title']"
#示例数据
data = {
        #"avatar":"../../../images/research-and-faculty/directory/chen-wei.jpg",
        #"name":"Wei Chen",
        "title":"Wilson-Cook Professor in Engineering Design",
        #"email":"abed@umd.edu"
        #"website":"http://www.ndcl.ee.psu.edu/index.asp",
        #"cooperation":"Chang Family Professor of Engineering Innovation ",
        }

#组织名
organization = "Northwestern University"

#主修专业
major = "Engineering"
#
# from utils.connection import *
# html=fetch("http://www.mccormick.northwestern.edu/research-faculty/directory/profiles/chen-wei.html")
# name = extract(avatar_rule, html)
# #print(name.xpath('string(.)'))
# print(name)