#coding:utf-8
"""
@file:      cbe_udel
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/6 9:38
@description:
            --
"""
#学者列表入口
base_url = 'http://www.cbe.udel.edu/directory/faculty.html'
#特征训练示例学者入口
sample_url = 'http://www.cbe.udel.edu/directory/facultyprofile.html?id=23383'
#条目链接
item_url_rule = "//tr/td/a/@href"
#个人简历规则
bio_rule = None
phone_rule = None
#示例数据
data = {"avatar":"http://www.cbe.udel.edu/images/faculty/23383.jpg",
        "name":"Maciek R Antoniewicz",
        "title":"Associate Professor",
        "phone":"302-831-8960",
        "email":"mranton@udel.edu ",
        "keywords":"Centennial Junior Professor of Chemical & Biomolecular Engineering"
        }

#组织名
organization = "University of Delaware"

#主修专业
major = "CHEMICAL & BIOMOLECULAR ENGINEERING"
