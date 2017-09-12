#coding:utf-8
"""
@file:      Sun_db_save
@author:    Lei Sun
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17/9/12 下午8:55
@description:
            --
"""
from utils.connection import *

def get_data(url,major):
    res = fetch(url)
    tmp = extract("//div[@class='col-xs-12 col-sm-12 col-md-9 col-lg-10 person']",res,multi=True)
    for a in tmp:
        name = extract("//h4/text()",html_source=str(etree.tostring(a))).replace('-','')
        email = extract("//p[contains(text(), '@')]/text()",html_source=str(etree.tostring(a))).replace('\xa0\xa0','').strip()
        web = extract("//div[@class='col-xs-12 col-sm-12 col-md-9 col-lg-10 person']/a/@href", str(etree.tostring(a)))
        organization = "Auburn University"
        print('name:',name)
        print('email:',email)
        print('organization:', organization)
        print("url:", web)
        print("major:", major)
        print("---------------------------")

get_data("http://eng.auburn.edu/aero/faculty/","Aerospace Engineering")
get_data("http://eng.auburn.edu/ece/faculty/","Electrical and Computer Engineering")

