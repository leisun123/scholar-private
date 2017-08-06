#coding:utf-8
"""
@file:      cse_nyu
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-7 上午12:31
@description:
            --
"""
#学者列表入口
base_url = 'http://engineering.nyu.edu/academics/departments/computer-science-engineering/people'
#特征训练示例学者入口
sample_url = 'http://engineering.nyu.edu/people/boris-aronov'
#条目链接
item_url_rule = "//div[@class='picture']/a/@href"

#填补缺失
bio_rule = None
phone_rule = None
avatar_rule = "//*[@id='center']/div/img/@src"


#示例数据
data = {#"avatar":"https://engineering.nd.edu/profiles/hfernando/@@images/fbd01446-37e5-43c7-8f8c-de8ff322f962.jpeg",
        "name":"Boris  Aronov",
        "title":"Professor",
        "phone":"646.997.3092",
        "email":"boris.aronov@nyu.edu",
        "website":"http://cis.poly.edu/~aronov/",
        #"cooperation":"College of Engineering",
        "keywords":"Computational, Combinatorial, and Discrete Geometry; Algorithms"
        }

#组织名
organization = "NYU Tandon School of Engineering"

#主修专业
major = "Chemical and Biomolecular Engineering"