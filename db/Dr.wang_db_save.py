#coding:utf-8
"""
@file:      Dr.wang_db_save
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/18 1:14
@description:
            --
"""
from db.SqlHelper import SqlHelper
from utils.logger import get_logger
import json
from nameparser import HumanName

def set_value(name, email, organization, website, major):
    
    keywordKeys = []
    cityKeys = []
    timeKeys = []
    
    keywords = []
    city = ["China"]
    time = ["Flexible"]
    
    parm = {
            "name":name,
            "email":email,
            "password":"dr.wang",
            "avatar":None,
            "profile":
                {
                "keywordKeys":[],
                "cityKeys":[1],
                "timeKeys":[1],
                "firstName":HumanName(name).first,
                "lastName":HumanName(name).last,
                "organization":organization,
                "major":major,
                "title":None,
                "birth":None,
                "country":None,
                "state":None,
                "city":["China"],
                "phone":None,
                "email":email,
                "website":website,
                "cooperation":[],
                "bio":None
                }
            }
    for i in keywordKeys:
        parm["profile"]["keyword-{}".format(i)] = keywords[i-1]
    for j in cityKeys:
        parm["profile"]["city-{}".format(j)] = city[j-1]
    for h in timeKeys:
        parm["profile"]["time-{}".format(h)] = time[h-1]
    return parm
sqlhepler = SqlHelper(logger=get_logger("dr.wang"))

with open("C:/Users/tonylu/Desktop/Bioengineering.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="lehigh University")
    sqlhepler.insert_scholar(**parm)
    
with open("C:/Users/tonylu/Desktop/school of Civil and Environmental Engineering.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="University of Massachusetts")
    sqlhepler.insert_scholar(**parm)

with open("C:/Users/tonylu/Desktop/communication.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="University of Massachusetts")
    sqlhepler.insert_scholar(**parm)

with open("C:/Users/tonylu/Desktop/school of Biochemistry and Molecular Biology.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="University of Massachusetts")
    sqlhepler.insert_scholar(**parm)

with open("C:/Users/tonylu/Desktop/school of Chemistry.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="University of Massachusetts")
    sqlhepler.insert_scholar(**parm)

with open("C:/Users/tonylu/Desktop/school of Electrical and computer engineering.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="University of Massachusetts")
    sqlhepler.insert_scholar(**parm)

with open("C:/Users/tonylu/Desktop/school of INformation and computer science.json",'r') as f:
    res = json.load(f)
for key,i in res.items():
    email = key
    name = i[0]
    website = i[2]
    major = i[3]
    parm = set_value(email=email, name=name, website=website, major=major, organization="University of Massachusetts")
    sqlhepler.insert_scholar(**parm)



















