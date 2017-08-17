#coding:utf-8
"""
@file:      SYL_db_save
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/18 1:14
@description:
            --
"""

from nameparser import HumanName

from utils.logger import get_logger


def set_value(name, email, organization, website, major, avatar):
    
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


from db.SqlHelper import SqlHelper
sqlhepler = SqlHelper(logger=get_logger("syl"))
import pymysql
conn = pymysql.connect(host='localhost',user='wyn',passwd='weiaizq1314',db='eb',port=3306)
cur = conn.cursor()
cur.execute("""
                  select * from sc;
                  """)
res= iter(cur.fetchall() )
while True:
    tmp = (next(res))
    name = tmp[0].replace("INSERT INTO `sc` VALUES ('","").replace("'","").strip()
    email = tmp[1]
    major = tmp[2]
    website = tmp[3]
    avatar = tmp[4]
    if "Texas" in major:
       organization =  "Texas A&M University"
    else:
       organization = "University of Southern California"
    
    # print("name:",name)
    # print("email",email)
    # print("avatar",avatar)
    # print("major",major)
    # print("website",website)
    # print("organzation",organzation)
    parm = set_value(name=name, email=email, avatar=avatar, major=major, organization=organization,
                     website=website)
    sqlhepler.insert_scholar(**parm)


    
    





























