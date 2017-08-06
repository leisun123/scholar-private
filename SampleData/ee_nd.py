#coding:utf-8
"""
@file:      ee_nd
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/5 15:56
@description:
            --
"""
#学者列表入口
base_url = 'http://www.ee.nd.edu/people/faculty'
#特征训练示例学者入口
sample_url = 'https://engineering.nd.edu/profiles/sdatta'
#条目链接
item_url_rule = "//a[@class='external-link']/@href"
#个人简历规则
bio_rule = "//h2[text()='Biography']/following-sibling::*/text()"
phone_rule = None
avatar_rule = "//*[@id='content-core']/p/img/@src"
cooperation_rule = "//p[@class='organisation']/strong/text()"
website_rule = "//ul[@class='profileLinks']/li[1]/a/@href"
#示例数据
data = {#"avatar":"https://engineering.nd.edu/profiles/pantsaklis/@@images/d55661c5-6a47-4932-af0d-0fbc0c9d5345.jpeg",
        "name":"Suman Datta",
        "title":"Chang Family Professor of Engineering Innovation",
        "phone":"574-631-8835",
        "email":"sdatta@nd.edu",
        #"website":"http://www.ndcl.ee.psu.edu/index.asp",
        #"cooperation":"Chang Family Professor of Engineering Innovation ",
        "keywords":"Department of Electrical Engineering"
        }

#组织名
organization = "UNIVERSITY of NOTRE DAME"

#主修专业
major = "Department of Electrical Engineering"

