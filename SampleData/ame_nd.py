#coding:utf-8
"""
@file:      ame.nd.edu
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/1 1:49
@description:
            --
"""
#学者列表入口
base_url = 'http://ame.nd.edu/people/faculty'
#特征训练示例学者入口
sample_url = 'https://engineering.nd.edu/profiles/hfernando'
#条目链接
item_url_rule = "//a[@class='external-link']/@href"
#示例数据
data = {"avatar":"https://engineering.nd.edu/profiles/hfernando/@@images/fbd01446-37e5-43c7-8f8c-de8ff322f962.jpeg",
        "name":"Harindra Fernando",
        "title":"Wayne and Diana Murdy Endowed Professor",
        "phone":"574-631-9346",
        "email":"Fernando.10@nd.edu",
        "website":"http://www.nd.edu/~dynamics/",
        "cooperation":"College of Engineering",
        "keywords":"Department of Aerospace and Mechanical Engineering"
        }

#组织名
organization = "UNIVERSITY of NOTRE DAME"

#主修专业
major = "Department of Aerospace and Mechanical Engineering"
