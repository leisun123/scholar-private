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
import os
import sys
from pprint import pprint
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from db.SqlHelper import SqlHelper
from utils.logger import get_logger
from utils.set_value import set_value
import simplejson
from utils.get_file_path import current_file_name
sqlhepler = SqlHelper(logger=get_logger("dr.wang"))

import os
tmp = "C:/Users/tonylu/Desktop/UConn"

def Wang_db_save(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.abspath(os.path.join(rootDir, lists))
        if os.path.isdir(path):
            Wang_db_save(path)
        else:
            with open(path, 'r') as f:
                res = simplejson.load(f)
            for key,i in res.items():
                if len(i) is 5:
                    email = key
                    name = i[0]
                    website = i[2]
                    major = i[3]
                    organization = i[4]
                elif len(i) is 4:
                    email = key
                    name = i[0]
                    website = i[2]
                    major = i[3]
                    organization = current_file_name(path)
                try:
                    parm = set_value(email=email, name=name, website=website, major=major, organization=organization)
                    sqlhepler.insert_scholar(**parm)
                except Exception as e:
                    print(e)
                    
Wang_db_save(tmp)



    
















