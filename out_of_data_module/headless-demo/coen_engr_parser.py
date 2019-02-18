# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: coen_engr_parser.py

@time: 12/25/18 17:08


'''

from utils.connection import *
from db.operateSql import People, connect_db
import time
from selenium import webdriver

db_url = "mysql+pymysql://root:123456@localhost/sc"
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

def get_info(url, org="Boise State University"):
    global majors
    majors = [
        "Civil Engineering",
        "Computer Science",
        "Construction Management",
        "Electrical & Computer Engineering",
        "Information Technology Services/COEN",
        "Organizational Performance and Workplace Learning",
        "Micron School of Materials Science and Engineering",
        "Mechanical & Biomedical Engineering",
        "Engineering Technical Services"
    ]
    try:
        html = fetch(url)
        urls = extract('//div[@id="faclistCol2"]//a[contains(@href, "/faculty-staff2")]/@href', html, True)
        for url in urls:
            web_url = url
            # browser = webdriver.Chrome()
            # browser.get(url)
            # res = browser.page_source
            res = fetch(url)
            major = extract("//div[@id='ContactInfo1']/text()[1]", res)
            if major and major not in majors:
                # browser.quit()
                continue
            print(major)
            # title = extract("//*[@id='ContactInfo1']/span/text()", res)
            name = extract("//div[@id='title']/h1/text()", res).split(',')[0]
            email = extract("//div[@id='ContactInfo1']//a[contains(@href, '@')]/text()", res)
            img_url = extract("//div[@id='rt_facBox']/img/@src", res)
            print(name, email, major, web_url, img_url, org)
            time.sleep(2)
            # save_info(name=name, email=email, web_url=web_url, org=org, img_url=img_url, major=major)
            # browser.quit()

    except:
        return get_info(url)


get_info("http://coen.boisestate.edu/faculty-staff2/?deptID=0")