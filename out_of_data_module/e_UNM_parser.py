# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: e_UNM_parser.py

@time: 2018/8/6 下午2:40


'''

import requests
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
    tmp = extract("//div[starts-with(@class,'single-person-entry')]", res, True)

    for each in tmp:
        source = str(etree.tostring(each))
        # print(source)
        title = extract("//span[@class='personlist-title']/text()", source)
        if title is not None and "Emeritus" in title:
            continue

        # print(title)

        # print(source)

        url = extract("//img[@class='left person-list']/@src", source)
        # print(url)
        if url is not None:
            pic_url = "http://engineering.unm.edu/faculty/directory/" + url
        else:
            pic_url = ""
        email = extract("//table/tr[1]/td[2]/a/@href", source)
        # print(email)
        if email is not None:
            email = email.split(':')[-1]
        else:
            continue
        name = extract("//h4/a/text()", source)
        web_url = extract("//h4/a/@href", source)
        if web_url is not None:
            web = "http://engineering.unm.edu/faculty/directory/" + web_url
        else:
            web = ""
        major = extract("//p[@class='areas']/text()", source)
        if major:
            major = "Department of " + major
        print(pic_url, " ", name, " ", email, " ", web, " ", major)
        try:
            pic = requests.Session().get(pic_url, timeout=30)
            with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg", "wb") as f:
                f.write(pic.content)
                f.close()
        except:
            with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                f.write(email + " : " + pic_url + "\n")
        user = People(email=email, name=name, major=major, web=web)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)


getInfo("http://engineering.unm.edu/faculty/directory/index.html")