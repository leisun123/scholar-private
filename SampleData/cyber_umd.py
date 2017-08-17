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
base_url = 'http://cyber.umd.edu/faculty'
#特征训练示例学者入口
sample_url = 'http://www.ece.umd.edu/faculty/abed'
#条目链接
item_url_rule = "//div[@class='view-content']/div/div[2]/span/a/@href"
avatar_rule = "//div[@class='field-item even']/img/@src"
website_rule = "//a[text()='Website']/@href"
#示例数据
data = {
        "name":"Abed, Eyad H.",
        "title":"Professor",
        "email":"abed@umd.edu"
        #"website":"http://www.ndcl.ee.psu.edu/index.asp",
        #"cooperation":"Chang Family Professor of Engineering Innovation ",
        }

#组织名
organization = "UNIVERSITY of MARYLAND"

#主修专业
major = "The Department of Electrical & Computer enginnering"

