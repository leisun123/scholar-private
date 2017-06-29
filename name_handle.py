#coding:utf-8
"""
@file:      name_handle
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/26 20:31
@description:
            --
"""
from Tool import nameparser

from ScholarClass import Scholar

s=Scholar
conn=s.connectdb()
cur=conn.cursor()
cur.execute(
    """
    SELECT
    """
)
