#coding:utf-8
"""
@file:      Wei_db_save
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/9/9 12:20
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from db.SqlHelper import *
from utils.logger import get_logger
from utils.set_value import set_value
import simplejson

sqlhelper = SqlHelper(logger=get_logger("wei"))

res = iter(sqlhelper.session.query(User).filter(User.email.contains("uic.edu")).all())

try:
    while True:
        i = next(res)
        object_attr = sqlhelper.session.query(ObjectAttribute).filter\
            (and_(ObjectAttribute.object_id==i.object_id, ObjectAttribute.name == 'profile')).first()
        
        sc_info = simplejson.loads(object_attr.value)
    
        try:
            if str(sc_info["profile"]["firstName"])[0:1] == 't':
                sc_info["profile"]["firstName"] = str(sc_info["profile"]["firstName"])[1:]
            sc_info = sc_info["profile"]
        except:
            print("Already Fix!")
        sqlhelper.session.close()
        parm = set_value(name=sc_info["firstName"]+sc_info["lastName"], email=i.email, \
                  organization=sc_info["organization"], website=sc_info["website"], major=sc_info["major"])
        sqlhelper.update_scholar(**parm)
except StopIteration:
    print("End")
    