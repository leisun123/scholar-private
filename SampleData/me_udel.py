#coding:utf-8
"""
@file:      me_udel
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/6 10:01
@description:
            --
"""
#学者列表入口
base_url = 'http://www.me.udel.edu/people/index.html'
#特征训练示例学者入口
sample_url = 'http://www.me.udel.edu/people/advani.html'
#条目链接
item_url_rule = "//tr/td/strong/a/@href"
#个人简历规则
bio_rule = "//h3[text()='Executive Summary']/following-sibling::*/text()"
phone_rule = None
#示例数据
data = {"avatar":"https://engineering.nd.edu/profiles/pantsaklis/@@images/d55661c5-6a47-4932-af0d-0fbc0c9d5345.jpeg",
        "name":"Panos Antsaklis",
        "title":"George W. Laird Professor",
        "phone":"574-631-5792",
        "email":"antsaklis.1@nd.edu",
        "website":"http://research.me.udel.edu/~advani",
        "keywords": "Department of Mechanical Engineering"
        }

#组织名
organization = "UNIVERSITY of NOTRE DAME"

#主修专业
major = "Department of Electrical Engineering"