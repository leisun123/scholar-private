#coding:utf-8
"""
@file:      cs_ucsb
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-13 下午6:00
@description:
            --
"""
#学者列表入口
base_url = 'http://www.cee.ucla.edu/faculty/'
#特征训练示例学者入口
sample_url = 'http://www.cee.ucla.edu/profile-bauchy/'
#条目链接

item_url_rule = "//tr/td[2]/a/@href"
avatar_rule = "//div/img/@src"
website_rule = "//*[contains(@class,'status-publish hentry category-uncategorized')]/div/div[1]/div/div/div/div/a[2]/@href"
email_rule ="//a[@class='mailto-link']/text()"
name_rule = "//h2"
title_rule = "//div[@clas='entry-content']/div[2]/div/div[2]/div/div/p[1]"

#示例数据
data = {
        "name_wrong":"Mathieu Bauchy, Ph.D."
        #"title":"Assistant Professor"
        #"email":"agrawal@cs.ucsb.edu"
        #"website":"http://www.ndcl.ee.psu.edu/index.asp",
        #"cooperation":"Chang Family Professor of Engineering Innovation ",
        }

#组织名
organization = "University of California"

#主修专业
major = "Civil and Environmental Enginnering"

