#coding:utf-8
"""
@file:      Li_db_save
@author:    Yu Li
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17/9/12 下午9:20
@description:
            --
"""
from utils.connection import *
def we():
    res = fetch("http://eng.auburn.edu/wireless/faculty/")
    res2 = extract("//div[@class='caption']", html_source=res, multi=True)
    
    print("----------------------------------------")
    major=extract("//h4/text()",res)
    for i in res2[1:]:
        name=extract("//h4/text()",str(etree.tostring(i)))
        href=extract("//a/@href",str(etree.tostring(i)))
        email = extract("//p[contains(text(),'@')]/text()", str(etree.tostring(i))).strip()
        organization = "Auburn University Samuel Ginn College of Engineering"
        
        print('name:',name.replace('-','').strip())
        print('website:',href)
        print('major:',major)
        print('email:',email)
        print('university:',organization)
        print("------------------------------------------")

def ce():
    res = fetch("http://eng.auburn.edu/civil/faculty/")
    res2 = extract("//div[@class='caption']", html_source=res, multi=True)
    major=extract("//h4/text()",res)
    for i in res2[1:]:
        name=extract("//h4/text()",str(etree.tostring(i)))
        href=extract("//a/@href",str(etree.tostring(i)))
        email = extract("//p[contains(text(),'@')]/text()", str(etree.tostring(i))).strip()
        organization = "Auburn University Samuel Ginn College of Engineering"
        print('name:',name.replace('-','').strip())
        print('website:',href)
        print('major:',major)
        print('email:',email)
        print('organization',organization)
        print("------------------------------------------")