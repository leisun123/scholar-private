#coding:utf-8
"""
@file:      ce_udel
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/6 10:43
@description:
            --
"""
#学者列表入口
base_url = 'http://www.ce.udel.edu/directories/faculty.html/'
#特征训练示例学者入口
sample_url = 'http://www.ce.udel.edu/directories/profiles.html?okine'
#条目链接
item_url_rule = "//tr/td/nobr/a/@href"
#个人简历规则
bio_rule = None
phone_rule = None
#示例数据
data = {"avatar":"http://www.ce.udel.edu/directories/headshots/12-Attoh-Okine-Nii.jpg",
        "name":"Nii O. Attoh-Okine",
        "title":"Professor",
        "phone":"(302) 831-4532",
        "email":"okine@udel.edu",
        }

#组织名
organization = "UNIVERSITY of NOTRE DAME"

#主修专业
major = "CIVIL & ENVIRONMENTAL ENGINEERING"

