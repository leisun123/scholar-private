#coding:utf-8
"""
@file:      civil_nyu
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-7 上午12:14
@description:
            --
"""
#学者列表入口
base_url = 'http://engineering.nyu.edu/academics/departments/civil/people/faculty'
#特征训练示例学者入口
sample_url = 'http://engineering.nyu.edu/people/fletcher-h-griffis'
#条目链接
item_url_rule = "//div[@class='user-profile']/h4/a/@href"

#填补缺失
bio_rule = "//*[@id='profile-pages-profile']/div[1]/div[1]"
phone_rule = None
avatar_rule = "//*[@id='center']/div/img/@src"


#示例数据
data = {#"avatar":"https://engineering.nd.edu/profiles/hfernando/@@images/fbd01446-37e5-43c7-8f8c-de8ff322f962.jpeg",
        "name":"Fletcher H. Griffis",
        "title":"Professor and Director",
        "phone":"646.997.3713",
        "email":"griffis@nyu.edu",
        #"website":"",
        #"cooperation":"College of Engineering",
        "keywords":"Civil and Urban Engineering; Center for Const. Management Innovation; NYS Resiliency Institute for Storms and Emergencies"
        }

#组织名
organization = "NYU Tandon School of Engineering"

#主修专业
major = "Civil and Urban Engineering"
