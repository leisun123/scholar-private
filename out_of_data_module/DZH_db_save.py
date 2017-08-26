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
from pprint import pprint

sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from nameparser import HumanName

from utils.logger import get_logger

from db.SqlHelper import SqlHelper
import pymysql
conn = pymysql.connect(host='localhost',user='wyn',passwd='weiaizq1314',db='scholar',port=3306)
cur = conn.cursor()
sqlhepler = SqlHelper(logger=get_logger("dzh"))
cur.execute("""
                  select * from json;
                  """)
#res= cur.fetchall()
from utils.pretty_dict import pretty_dict
import simplejson
for i in cur:
    #sqlhepler.insert_scholar(**(simplejson.loads(i[1])))
    tmp = simplejson.loads(i[1])
    tmp["firstName"] = HumanName(tmp["name"]).first
    tmp["lastName"] = HumanName(tmp["name"]).last
    if "osu" in tmp["email"]:
        tmp["profile"]["organization"] = "The Ohio State University"
    if "oci" in tmp["email"]:
        tmp["profile"]["organization"] = "University of California, Irvine"
    if "umd" in tmp["email"]:
        tmp["profile"]["organization"] = "The University of Maryland"
    #print(tmp["firstName"], tmp["lastName"], tmp["profile"]["organization"])
    sqlhepler.update_scholar(**tmp)