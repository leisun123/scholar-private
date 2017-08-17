#coding:utf-8
"""
@file:      me_umn
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-14 下午4:11
@description:
            --
"""

#学者列表入口
base_url = 'http://www.me.umn.edu/people/index.shtml'
#特征训练示例学者入口
sample_url = 'http://www.me.umn.edu/people/abel.shtml'
#条目链接
item_url_rule = "//span[@class='style2']/a/@href"
avatar_rule = "//div[@class='grid_3']/p/img/@src"
#website_rule = "//a[text()='Website']/@href"
#示例数据
data = {
        "name":"Julianna Abel",
        #"title":"Professor",
        "email":"jabel@umn.edu"
        #"website":"http://www.ndcl.ee.psu.edu/index.asp",
        #"cooperation":"Chang Family Professor of Engineering Innovation ",
        }

#组织名
organization = "University of Minnesota"

#主修专业
major = "Mechanical Enginnering"

