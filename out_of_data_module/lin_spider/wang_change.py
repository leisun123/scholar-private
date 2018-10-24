# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: wang_change.py

@time: 2018/7/18 下午9:41


'''

from utils.connection import *
import time
from db.operateSql import People, connect_db

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url):
    try:
        res = fetch(url)
    except:
        return getInfo(url)
    tmp = extract("//div[@class='column small-12 medium-4']", res, True)


    for each in tmp:
        source = str(etree.tostring(each))
        name = extract("//span[@class='name-first profile-name']/text()", source) + " " + \
            extract("//span[@class='name-last profile-name']/text()", source)
        web_url = extract("//div[@class='profile-card-name-container']/h1/a/@href", source)
        if web_url is not None:
            web = "http://www.engr.ucr.edu" + web_url
            print(web)
            try:
                html = fetch(web)
                major = extract("//p[@class='contact-dept']/text()", html)
            except:
                pass

        else:
            web = ""
        email = extract("//li[@class='email']/span/a/text()", source)

        print(name, " ", email, " ", web, " ", major)
        user = People(email=email, name=name, major=major, web=web)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)


getInfo("http://www.engr.ucr.edu/people/index.html")