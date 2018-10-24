# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: cse_SUNY_parser.py

@time: 2018/7/13 下午7:03


'''

import requests
from utils.connection import *
import time
from db.operateSql import People, connect_db

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url, major):
    try:
        res = fetch(url)
    except:
        return getInfo(url, major)
    tmp = extract("//div[@class='staffdirectory imagebase section']", res, True)


    for each in tmp:
        source = str(etree.tostring(each))

        # print(source)
        url = extract("//div[@class='staff_photo ']/a/picture/img/@src", source)
        if url is not None:
            pic_url = "http://engineering.buffalo.edu/" + url
        else:
            pic_url = ""
        email = extract("//a[@class='longtext']/@href", source).split(':')[-1]
        name = extract("//span[@class='staff_name_bolded']/a/text()", source)
        web_url = extract("//span[@class='staff_name_bolded']/a/@href", source)
        if web_url is not None:
            web = "http://engineering.buffalo.edu/" + web_url
        else:
            web = ""
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

getInfo("http://engineering.buffalo.edu/civil-structural-environmental/people/faculty_directory.html",\
        "Department of Civil, Structural and Environmental Engineering")