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
avatar_rule = "//*[@id='content']/div[1]/img/@src"
email_rule = "//*[@id='content']/div[1]/p[1]/a/text()"
website_rule = "//*[@id='content']/div[1]/p[2]/a/@href"


#示例数据
data = {#"avatar":"https://engineering.nd.edu/profiles/pantsaklis/@@images/d55661c5-6a47-4932-af0d-0fbc0c9d5345.jpeg",
        "name":"Dr. Suresh G. Advani",
        #"title":"George W. Laird Professor",
        #"phone":"574-631-5792",
        #"email":"advani@udel.edu",
        #"website":"http://research.me.udel.edu/~advani",
        #"keywords": "Department of Mechanical Engineering"
        }

#组织名
organization = "University of Delaware"

#主修专业
major = "MECHANICAL Engineering"