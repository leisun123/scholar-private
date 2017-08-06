#coding:utf-8
"""
@file:      engineering_nyu
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/6 11:16
@description:
            --
"""
#学者列表入口
base_url = 'http://engineering.nyu.edu/academics/departments/biomolecular/people#core'
#特征训练示例学者入口
sample_url = 'http://engineering.nyu.edu/people/stephen-arnold'
#条目链接
item_url_rule = "//div[@class='user-profile']/h4/a/@href"

#填补缺失
bio_rule = None
phone_rule = None
avatar_rule = "//*[@id='center']/div/img/@src"


#示例数据
data = {#"avatar":"https://engineering.nd.edu/profiles/hfernando/@@images/fbd01446-37e5-43c7-8f8c-de8ff322f962.jpeg",
        "name":"Stephen   Arnold",
        "title":"University Professor",
        "phone":"646.997.3899, (917) 568-6549",
        "email":"sa1577@nyu.edu",
        "website":"http://www.mp3l.org",
        #"cooperation":"College of Engineering",
        "keywords":"Physics and Chemistry"
        }

#组织名
organization = "NYU Tandon School of Engineering"

#主修专业
major = "Chemical and Biomolecular Engineering"