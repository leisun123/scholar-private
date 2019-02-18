# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: engr_CUNY_parser.py

@time: 12/3/18 15:49


'''

from utils.connection import *
from db.operateSql import People, connect_db
from utils.selenuim_parser import SelenuimParser
from selenium import webdriver
import time

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, org="CUNY--City College (Grove)"):
    global img_url
    # browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=2))
    browser = webdriver.Chrome()
    try:
        browser.get(url)
    except Exception as e:
        print(e)
        browser.execute_script('window.stop()')
    finally:
        tmp = browser.find_elements_by_xpath("//ul[@id='list-staff']/li")

    for i in tmp:
        each = i.get_attribute('innerHTML')
        web = extract("//h3[@class='desktop']/a/@href", each)
        if web:
            web_url = "https://www.ccny.cuny.edu" + web
        else:
            web_url = ""
        email = extract("//a[contains(@href, '@')]/text()", each)
        # print(email)
        name = extract("//h3[@class='desktop']/a/text()", each)
        img_url = extract("//div[@class='lFloatGraphic']/a/img/@src", each)
        major = extract("//div[@class='inner2 floatLeft']/h4/text()", each)
        print(name, email, major, web_url, img_url, org)

        user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
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
    browser.quit()


for i in range(0, 9):
    print(str(i))
    get_info(url="https://www.ccny.cuny.edu/people?cat=1&school=21&dept=All&page=" + str(i))
