#coding:utf-8
"""
@file:      set_value
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/31 14:02
@description:
            --
"""
from nameparser import HumanName
def set_value(name, email, organization, website, major, avatar=None):
    
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
            "avatar":avatar,
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