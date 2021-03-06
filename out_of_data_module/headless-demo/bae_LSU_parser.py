# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: bae_LSU_parser.py

@time: 2018/10/18 上午10:57


'''

from utils.connection import *
from db.operateSql import People, connect_db
import time


db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, major):
    global img_url
    try:
        html = fetch(url)
        tmp = extract('//*[@id="maincontent"]/div/div/table/tbody/tr', html, True)
        # print(tmp)
    except:
        return get_info(url, major)

    for i in tmp:
        each = str(etree.tostring(i))
        # print(each)
        title = extract("//td[3]/div[2]/text()", each)
        # print(title)
        if title and "Professor" not in str(title):
            continue
        name = extract("//a[contains(@href, '/eng/bae')]/text()", each)
        # if not name:
        #     continue
        img = extract("//img/@src", each)
        if img:
            img_url = "https://www.lsu.edu" + img
        email = extract("//a[contains(@href, '@')]/text()", each)
        if not email:
            continue
        web = extract("//a[contains(@href, '/eng/bae')]/@href", each)
        if web:
            web_url = "https://www.lsu.edu" + web
        else:
            web_url = ""
        print(name, email, major, web_url, img_url, title)
        user = People(email=email, name=name, major=major, web=web_url)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)
        if img_url is not None and email is not None:
            # img = "http://be.utdallas.edu" + img_url
            print(img_url)
            try:
                pic = requests.Session().get(img_url, timeout=30)
                with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
                          "wb") as f:
                    f.write(pic.content)
                    f.close()
            except:
                with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    f.write(email + " : " + img_url)
                    f.close()


get_info("https://www.lsu.edu/eng/bae/people/faculty-instructors.php",\
         "Department of Biological and Agricultural Engineering")