#coding:utf-8
"""
@
+
*ile:      test
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    8/24/17 9:52 PM
@description:
            --
"""
import os
import sys

from nameparser import HumanName
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from utils.logger import get_logger
from utils.connection import *
from db.SqlHelper import SqlHelper
from utils.set_value import set_value
sqlhelper = SqlHelper(logger=get_logger("wz"))

    

def bme():
    html = fetch("https://bme.ucdavis.edu/people/departmental-faculty/")
    item_list = extract("//tbody/tr", html, multi=True)
    for i in item_list:
        avatar = extract("//td[1]/a/img/@src", str(etree.tostring(i)))
        name = extract("//td[2]/a/strong/text()", str(etree.tostring(i)))
        major = "Biomedical Engineering"
        organzation = "University of California,Davis"
        website = extract("//a[@rel='noopener noreferrer']/@href", str(etree.tostring(i)))

        if extract("//td[2]/a/@href", str(etree.tostring(i))) is not None:
            sc_url = extract("//td[2]/a/@href", str(etree.tostring(i)))
        elif extract("//td[2]/p[1]/a/@href", str(etree.tostring(i))) is not None:
            sc_url = extract("//td[2]/p[1]/a/@href", str(etree.tostring(i)))
        else:
            sc_url = extract("//td[2]/p[1]/strong/a/@href", str(etree.tostring(i)))
        
        try:
            ht = fetch(sc_url)
            emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
            import re
            email = re.search(emailRegex, ht).group(0)
        except:
            pass
        
        print(avatar)
        print(name)
        print(website)
        print(email)
        print("--------------------------------------------")
        try:
            parm = set_value(avatar=avatar, name=name, website=website, email=email, organization=organzation, major=major)
        except:
            pass
        sqlhelper.insert_scholar(**parm)
    print("End")
#bme()

def che():
    html = fetch("https://che.engineering.ucdavis.edu/people/faculty/")
    item_list = extract("//table[1]/tbody/tr", html, multi=True)
    for i in item_list:
        avatar = extract("//td[1]/img/@src", str(etree.tostring(i)))
        name = extract("//td[2]/h4/a/text()", str(etree.tostring(i)))
        major = "Chemical Enginnering"
        organzation = "University of California,Davis"
        website = "https://che.engineering.ucdavis.edu/people/faculty/"
        email = extract("//td[2]/p/a/text()", str(etree.tostring(i)))
        print(avatar)
        print(name)
        print(website)
        print(email)
        print("--------------------------------------------")
        try:
            parm = set_value(avatar=avatar, name=name, website=website, email=email, organization=organzation, major=major)
        except:
            pass
        sqlhelper.insert_scholar(**parm)
    print("End")


def cee():
    html = fetch("http://cee.engr.ucdavis.edu/people/faculty-directory/")
    item_list = extract("//table/tbody/tr", html, multi=True)
    for i in item_list[1:]:
        sc_url = extract("//td[1]/a/@href", str(etree.tostring(i)))
        name = extract("//td[1]/a/span/text()", str(etree.tostring(i)))
        if name is None:
            name = extract("//td[1]/a/text()", str(etree.tostring(i)))
        major = "Civil and Environmental Engineering"
        organzation = "University of California,Davis"
        try:
            ht = fetch(sc_url)
            website = sc_url
        except:
            website = ""
        
        
        if extract("//div[@class='entry-content']/p[2]", ht) is not None:
            tmp = extract("//div[@class='entry-content']/p[2]", ht).xpath('string(.)')
        if "Email" not in tmp:
            if extract("//div/div/p[2]", ht) is not None:
                tmp = extract("//div/div/p[2]", ht).xpath('string(.)')
        if tmp:
                a = tmp.split('\n')[0].replace('Email:','').replace('at','@').strip()
                if '.' in a:
                    email = (a.split('edu')[0] + 'edu').replace(' ','')
                elif "Phone" in a:
                    pass
                else:
                    email = (a.split('edu')[0] + 'edu').replace(' ','')
        avatar = extract("//div[@id='facultysidebar']/a/img/@src", ht)
        print(avatar)
        print(name)
        print(website)
        print(email)
        print("--------------------------------------------")
        try:
            parm = set_value(avatar=avatar, name=name, website=website, email=email, organization=organzation, major=major)
        except:
            pass
        sqlhelper.insert_scholar(**parm)
    print("End")
#cee()

def mse():
    html = fetch("https://mse.engineering.ucdavis.edu/people/faculty/")
    item_list = extract("//table[1]/tbody/tr", html, multi=True)
    for i in item_list:
        avatar = extract("//td[1]/img/@src", str(etree.tostring(i)))
        name = extract("//td[2]/h4/a/text()", str(etree.tostring(i)))
        email = extract("//td[2]/p/a/text()", str(etree.tostring(i)))
        website = extract("//td[2]/h4/a/@href", str(etree.tostring(i)))
        organzation = "University of California,Davis"
        major = "Materials Science And Engineering"
        print(avatar)
        print(name)
        print(website)
        print(email)
        print("-----------------------------------------------------------")
        try:
            parm = set_value(avatar=avatar, name=name, website=website, email=email, organization=organzation, major=major)
        except:
            pass
        sqlhelper.insert_scholar(**parm)
    print("End")
#mse()

def mae():
    html = fetch("http://mae.ucdavis.edu/people/faculty/")
    item_list = extract("//div[@id='post-1984']/p", html, multi=True)
    name_list = extract("//div[@id='post-1984']/h3/text()", html, multi=True)
    for i,j in zip(item_list,name_list):
        name = j
        website = extract("//a[1]/@href", str(etree.tostring(i)))
        email = extract("//a[2]/text()", str(etree.tostring(i)))
        organzation = "University of California,Davis"
        major = "Mechanical and Aerospace Engineering"
        avatar = None
        print(name)
        print(website)
        print(email)
        try:
            parm = set_value(avatar=avatar, name=name, website=website, email=email, organization=organzation, major=major)
            sqlhelper.insert_scholar(**parm)
        except:
            pass
    print("End")
#mae()

def ece():
    html = fetch("https://www.ece.ucdavis.edu/people/faculty/")
    item_list = extract("//div[@id='post-2013']/ul/li/a/@href", html, multi=True)
    name_list = extract("//div[@id='post-2013']/ul/li/a/text()", html, multi=True)
    for i, j in zip(item_list, name_list):
        name = ''.join(j.split(',')[:-1]).replace(',','')
        
        try:
            ht = fetch(i)
        except:
            continue
        if extract("//li[contains(text(),'Email')]/text()", ht) is not None:
            email = extract("//li[contains(text(),'Email')]/text()", ht).replace('Email:','').\
                replace('at','@').replace(' ','')[1:]
        website = i
        organaztion = "University of California,Davis"
        major = "Electrical And Computer Engineering"
        avatar = extract("//*[@id='facultysidebar']/a[1]/img/@src", ht)
        print(name)
        print(website)
        print(email)
        print(avatar)
        try:
            parm = set_value(avatar=avatar, name=name, website=website, email=email, organization=organaztion, major=major)
            sqlhelper.insert_scholar(**parm)
        except:
            pass
        
        
    print('End')
ece()

# def cs():
#     html = fetch("http://www.cs.ucdavis.edu/people/faculty/")
#     item_list = extract("//ul/li/a/@href", html)
#     name_list = extract("//ul/li/a/text()", html)
#     for i, j in zip(item_list, name_list):
#         name = j
#         ht = fetch(i)
        