#coding:utf-8
"""
@file:      SqlHelper
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/29 23:12
@description:
            --
"""
import datetime
from sqlalchemy import Column,Integer,String,DateTime,Numeric,create_engine,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

from db.ISqlHelper import ISqlHelper

BaseModel = declarative_base()
class Article(BaseModel):
    __tablename__='article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(VARCHAR(200),nullable=False)
    url = Column(VARCHAR(200),nullable=)
    