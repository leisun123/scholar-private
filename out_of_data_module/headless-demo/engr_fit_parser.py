# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: engr_fit_parser.py

@time: 1/6/19 11:52


'''

from utils.connection import *
from db.operateSql import People, connect_db
import time
from selenium import webdriver
from utils.selenuim_parser import SelenuimParser
from ScholarConfig.config import DB_CONFIG

db_url = DB_CONFIG['DB_CONNECT_STRING']
session = connect_db(db_url)


def save_info(name, email, web_url, img_url, major, org):
    user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
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
            with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
                      "wb") as f:
                f.write(pic.content)
                f.close()
        except:
            with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                f.write(email + " : " + img_url)
                f.close()


def get_info(url, org="Florida Institute of Technology"):
    global name
    try:
        html = fetch(url)
        # browser = webdriver.Chrome()
        # browser.get(url)
        # html = browser.page_source
        major = extract('//*[@id="page-content"]/div[1]/div/a[3]/text()', html)
        urls = extract('//div[@id="page-content"]/p//a[contains(@href, "http")]/@href', html, True)
        print(urls)
        for url in urls:
            if url is None:
                continue
            else:
                web_url = url
                browser = webdriver.Chrome()
                # browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=1))
                browser.get(url)
                res = browser.page_source
                # res = fetch(url)
                # title = extract("//*[@id='ContactInfo1']/span/text()", res)
                email = extract("//div[@class='four wide computer column sidebar']//p//a[contains(@href, '@')]/text()", res)
                if not email:
                    continue
                fullname = extract("//div[@class='twelve wide computer column']/h2/text()", res)
                if "," in fullname:
                    name = fullname.split(',')[1].strip() + " " + fullname.split(',')[0].strip()
                else:
                    name = fullname
                img = extract("//div[@class='four wide computer column sidebar']//p/img/@src", res)
                if img:
                    img_url = "https://www.fit.edu" + img
                else:
                    img_url = ""
                print(name, email, major, web_url, img_url, org)
                time.sleep(2)
                save_info(name=name, email=email, web_url=web_url, org=org, img_url=img_url, major=major)
                browser.quit()
    except:
        return get_info(url)


# get_info("https://www.fit.edu/engineering-and-science/academics-and-learning/aerospace-physics-and-space-sciences/faculty/")
# get_info("https://www.fit.edu/engineering-and-science/academics-and-learning/biomedical-and-chemical-engineering-and-sciences/faculty/")
# get_info("https://www.fit.edu/engineering-and-science/academics-and-learning/computer-engineering-and-sciences/faculty-/")
# get_info("https://www.fit.edu/engineering-and-science/academics-and-learning/mathematical-sciences/faculty-/")
# get_info("https://www.fit.edu/engineering-and-science/academics-and-learning/mechanical-and-civil-engineering/faculty-/")
get_info("https://www.fit.edu/engineering-and-science/academics-and-learning/ocean-engineering-and-marine-sciences/faculty-/")