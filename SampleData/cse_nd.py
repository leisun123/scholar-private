#coding:utf-8
"""
@file:      cse_nd
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/5 15:07
@description:
            --
"""
#学者列表入口
base_url = 'http://cse.nd.edu/people/faculty'
#特征训练示例学者入口
sample_url = 'https://engineering.nd.edu/profiles/kbowyer'
#条目链接
item_url_rule = "//a[@class='external-link']/@href"
#个人简历规则
bio_rule = "//h2[text()='Biography']/following-sibling::*/text()"
phone_rule = None
#示例数据
data = {"avatar":"https://engineering.nd.edu/profiles/kbowyer/@@images/cba516c9-5234-4620-a738-93b796bc7e15.jpeg",
        "name":"Kevin W. Bowyer",
        "title":"Schubmehl-Prein Professor",
        "phone":"574-631-9978",
        "email":"kwb@nd.edu",
        "website":"http://www.nd.edu/~kwb",
        "cooperation":"Department of Computer Science and Engineering",
        "keywords":"College of Engineering"
        }

#组织名
organization = "UNIVERSITY of NOTRE DAME"

#主修专业
major = "Department of Computer Science and Engineering"