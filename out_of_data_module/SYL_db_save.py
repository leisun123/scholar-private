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
import os
import sys

sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))



from utils.logger import get_logger
from utils.set_value import set_value

from db.SqlHelper import SqlHelper
import pymysql
conn = pymysql.connect(host='localhost',user='wyn',passwd='weiaizq1314',db='eb',port=3306)
cur = conn.cursor()
sqlhepler = SqlHelper(logger=get_logger("syl"))
cur.execute("""
                  select * from sc;
                  """)
res= iter(cur.fetchall() )

while True:
    tmp = (next(res))
    name = tmp[0].replace("INSERT INTO `sc` VALUES ('","").replace("'","").strip()
    email = tmp[1].replace("'","")
    major = tmp[2].replace("'","")
    website = tmp[3].replace("'","")
    avatar = tmp[4].replace("'","").replace(");","")
    if "Texas" in major:
       organization =  "Texas A&M University"
    else:
       organization = "University of Southern California"
    
    # print("name:",name)
    # print("email:",email)
    # print("avatar:",avatar)
    # print("major:",major)
    # print("website:",website)
    # print("organzation:",organization)
    parm = set_value(name=name, email=email, avatar=avatar, major=major, organization=organization,
                     website=website)
    try:
        sqlhepler.update_scholar(**parm)
    except:
        pass
    
    





























