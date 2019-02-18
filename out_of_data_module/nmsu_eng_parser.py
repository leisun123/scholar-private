# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: nmsu_eng_parser.py

@time: 12/25/18 15:35


'''

from utils.connection import *
import time
from db.operateSql import People, connect_db

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url, major, org="New Mexico State University"):
    try:
        res = fetch(url)
    except:
        return getInfo(url, major, org)
    tmp = extract("//div[@class='entry-content']/table[1]/tbody/tr", res, True)
    # print(tmp)

    for each in tmp:
        source = str(etree.tostring(each))

        # print(source)
        email = extract("//a[contains(@href, '@')]/@href", source)
        if not email:
            continue
        else:
            email = email.split(':')[1]
        fullname = extract("//td[1]/a[text()]/text()", source)
        if fullname:
            web_url = extract("//td[1]/a/@href", source)
            name = fullname.split(',')[1] + " " + fullname.split(',')[0]
        else:
            # fullname = extract("//td[1]/a[text()]/text()", source)
            name = ""
        # name = fullname.split(',')[1] + " " + fullname.split(',')[0]
        # print(web_url)
        img_url = extract("//td[1]//img/@src", source)
        # print(name)
        print(img_url, " ", name, " ", email, " ", web_url, " ", major, " ", org)
        if img_url:
            try:
                pic = requests.Session().get(img_url, timeout=30)
                with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg", "wb") as f:
                    f.write(pic.content)
                    f.close()
            except:
                with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    f.write(email + " : " + img_url + "\n")
        user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)


getInfo("https://mae.nmsu.edu/faculty/",
        "Department of Mechanical & Aerospace Engineering")
