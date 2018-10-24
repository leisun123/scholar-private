# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: cb_SUNY_parser.py

@time: 2018/7/13 上午8:01


'''

from utils.connection import *
import requests
import time
from db.operateSql import People
from db.operateSql import connect_db


# book = xlwt.Workbook(encoding="UTF-8")
# sheet = book.add_sheet("孙磊")
# sheet.write(0, 0, "name")
# sheet.write(0, 1, "email")
# sheet.write(0, 2, "major")
# sheet.write(0, 3, "web")
# book.save("/Users/sunlei/scholar-private/out_of_data_module/scholar.xls")

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)

def getInfo(url, major):
    try:
        res = fetch(url)
    except:
        return getInfo(url, major)
    tmp = extract("//div[@class='profilepage unstructuredpage page']", res, True)

    for each in tmp:
        source = str(etree.tostring(each))
        try:
            # print(source)
            url = extract("//div[@class='profileinfo-teaser-photo']/picture/img/@src", source)
            if url is not None:
                pic_url = "http://engineering.buffalo.edu/" + url
            else:
                pic_url = ""
            email = extract("//a[@class='longtext']/@href", source).split(':')[-1]
            name = extract("//a[@class='title']/b/text()", source)
            web_url = extract("//a[@class='title']/@href", source)
            if web_url is not None:
                web = "http://engineering.buffalo.edu/" + web_url
            else:
                web = ""
            print(pic_url, " ", name, " ", email, " ", web, " ", major)

            # sheet.write(n, 0, name)
            # sheet.write(n, 1, email)
            # sheet.write(n, 2, major)
            # sheet.write(n, 3, web)
            # book.save("/Users/sunlei/scholar-private/out_of_data_module/scholar.xls")
            try:
                pic = requests.Session().get(pic_url, timeout=20)
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
        except Exception as e:
            print(e)

major = "Department of Chemicaland Biological Engineering"

getInfo("http://engineering.buffalo.edu/chemical-biological/people/faculty-directory.html", major)
getInfo("http://engineering.buffalo.edu/chemical-biological/people/faculty-directory.teaching.html", major)
getInfo("http://engineering.buffalo.edu/chemical-biological/people/faculty-directory.research.html", major)