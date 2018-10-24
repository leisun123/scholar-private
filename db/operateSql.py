# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: operateSql.py

@time: 2018/7/14 下午12:48


'''

from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class People(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True)
    name = Column(String(32))
    major = Column(String(96))
    web = Column(String(500))

def connect_db(mysql_url):
    engine = create_engine(mysql_url, encoding="utf-8")
    DBsession  = sessionmaker(engine)
    return DBsession()

url = "mysql+pymysql://root:123456@localhost/sc"
connect_db(url)
Base.metadata.create_all(create_engine(url, encoding="UTF-8"))