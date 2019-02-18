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
import requests
import time

Base = declarative_base()


class People(Base):       #建立数据表
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True)
    name = Column(String(32))
    major = Column(String(96))
    web = Column(String(500))
    orginazation = Column(String(64))


def connect_db(mysql_url):
    engine = create_engine(mysql_url, encoding="utf-8")
    engine.execute('set names utf8')
    DBsession  = sessionmaker(engine)
    return DBsession()


from ScholarConfig.config import DB_CONFIG

db_url = DB_CONFIG['DB_CONNECT_STRING']



def save_info(name,       #将数据储存到数据库中
              email,
              web_url,
              img_url,
              major,
              org):
    user = People(email=email,
                  name=name,
                  major=major,
                  web=web_url,
                  orginazation=org)
    session = connect_db(DB_CONFIG['DB_CONNECT_STRING'])
    session.add(user)
    try:
        session.commit()
    except:
        session.rollback()
    time.sleep(1)
    if img_url is not None and email is not None:
        print(img_url)
        try:
            pic = requests.Session().get(img_url, timeout=30)
            with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",   #保存图片路径
                      "wb") as f:
                f.write(pic.content)
                f.close()
        except:
            with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:   #图片下载失败链接
                f.write(email + " : " + img_url + "\n")
                f.close()


connect_db(db_url)
Base.metadata.create_all(create_engine(db_url, encoding="UTF-8"))