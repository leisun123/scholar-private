# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: eng_sdsu_parser.py

@time: 12/9/18 20:16


'''


from utils.connection import *
import time
from db.operateSql import People
from db.operateSql import connect_db
from selenium import webdriver
from utils.selenuim_parser import SelenuimParser


db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, major, org="San Diego State University"):
    global img_url
    try:
        browser = webdriver.Chrome()
        # html = fetch(url)
        browser.get(url)
        # tmp = extract("//div[@class='container']/table[@width='100%']/tbody/tr", html, True)
        tmp = browser.find_elements_by_xpath("//table[@width='100%']/tbody/tr")
        # print(tmp)

    except Exception as e:
        print(e)
        return get_info(url, major)

    for i in tmp:
        # each = str(etree.tostring(i))
        each = i.get_attribute('innerHTML')
        # print(each)
        img = extract("//td[2]/img/@src", each)
        if img:
            img_url = "http://ccee.sdsu.edu" + img
        # print(img)
        web_url = extract("//td[5]/a/@href", each)
        if not web_url:
            web_url = ""
        name = extract("//td[3]/p/text()", each)
        email = extract("//td[6]/a/@href", each)
        if email:
            email = email.split(':')[1]
        else:
            continue
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
            # print(img_url)
            try:
                pic = requests.Session().get(img_url, timeout=300)

                with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
                          "wb") as f:
                    f.write(pic.content)
                    f.close()
            except Exception as e:
                print(e)
                print(img_url)
                with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    f.write(email + " : " + img_url + "\n")
                    f.close()


get_info("https://electrical.sdsu.edu/faculty.php",
         "Department of Electrical and Computer Engineering")
