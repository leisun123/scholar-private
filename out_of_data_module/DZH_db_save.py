#coding:utf-8
"""
@file:      DZH_db_save
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/18 1:15
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from nameparser import HumanName
from utils.logger import get_logger
from utils.set_value import set_value
from db.SqlHelper import SqlHelper
import pymysql
conn = pymysql.connect(host='localhost',user='wyn',passwd='weiaizq1314',db='eb',port=3306)
cur = conn.cursor()
sqlhepler = SqlHelper(logger=get_logger("dzh"))
cur.execute("""
                  select * from json;
                  """)
#res= cur.fetchall()
from utils.pretty_dict import pretty_dict
# import simplejson
# for i in cur:
#     #sqlhepler.insert_scholar(**(simplejson.loads(i[1])))
#     try:
#         tmp = simplejson.loads(i[1])
#         tmp["profile"]["firstName"] = HumanName(tmp["name"]).first
#         tmp["profile"]["lastName"] = HumanName(tmp["name"]).last
#         #print(tmp["firstName"], tmp["lastName"], tmp["profile"]["organization"], tmp["profile"]["email"], tmp["profile"]["webiste"])
#         #print(tmp)
#         sqlhepler.insert_scholar(**tmp)
#     except:
#         print(i)
# print("---------------------End----------------------------")
#
print(cur.fetchall())