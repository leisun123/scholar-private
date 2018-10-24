# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: cs_wpi.py

@time: 2018/8/28 下午8:21


'''

from utils.connection import *
from selenium import webdriver
import time
from db.operateSql import People, connect_db


db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url, major):
    try:
        browser = webdriver.PhantomJS()
        browser.get(url)
    except:
        return getInfo(url, major)
    tmp = browser.find_elements_by_xpath("//section[@aria-label='directory-table']/div")
    print(len(tmp))
    for each in tmp:
        source = each.get_attribute("innerHTML")

        # print(source)
        pic_url = extract("//div[@class='member-photo']/img/@src", source)
        # print(url)
        if not url:
            pic_url = ""
        email = extract("//*[contains(@href, '@')]/text()", source)
        if email is not None:
            email = str(email).split(':')[-1].split('"')[0]
        else:
            continue
        name = extract("//div[@class='member-photo']/img/@alt", source)
        if not name:
            continue
        web_url = extract("//*[@class='name']/a/@href", source)
        if web_url:
            web = "https://www.wpi.edu/" + web_url
        else:
            web = ""
        print(pic_url, " ", name, " ", email, " ", web, " ", major)
        try:
            pic = requests.Session().get(pic_url, timeout=30)
            with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg", "wb") as f:
                f.write(pic.content)
                f.close()
        except Exception as e:
            print(e)
            with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                f.write(email + " : " + pic_url + "\n")
        user = People(email=email, name=name, major=major, web=web)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)


getInfo("https://www.wpi.edu/academics/departments/computer-science/faculty-staff", \
        "Department of Computer Science")
