# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: eng_UARK_parser.py

@time: 11/8/18 12:40 PM


'''


from utils.connection import *
import random
from db.operateSql import People, connect_db
from selenium.webdriver.chrome.options import Options
import time
from utils.selenuim_parser import SelenuimParser
from selenium import webdriver

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, major, org):
    global img_url
    try:
        # html = fetch(url)
        browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=2))
        # chrome_options = Options()
        # prefs = {
        #     'profile.default_content_setting_values': {
        #         'images': 2,
        #         'javascript': 2
        #     }
        # }
        # chrome_options.add_experimental_option('prefs', prefs)
        # chrome_options.add_argument('--headless')
        # browser = webdriver.Chrome(chrome_options=chrome_options)
            # browser.get(web_url)
        browser.get(url)
        tmp = browser.find_elements_by_xpath("//div[@class='col-sm-3 col-md-3 col-xs-6 uark-unify-heights']")
        # print(tmp)
    except:
        return get_info(url, major, org)

    for i in tmp:
        source = i.get_attribute("innerHTML")
        # print(source)
        email = extract("//div[@class='email']/a/text()", source)
        if not email:
            continue
        web = extract("//a[1]/@href", source)
        name = extract("//div[@class='name']/text()", source)
        if web:
            web_url = "https:" + web
        else:
            web_url = ""
        img = extract("//img[@class='img-responsive img-thumbnail']/@src", source)
        if img:
            img_url = "https:" + img
            # print(img_url)
        else:
            img_url = ""
        print(name, email, major, web_url, img_url, org)
        user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
        session.add(user)
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
        time.sleep(1)
        if img_url is not None and email is not None:
            # img = "http://be.utdallas.edu" + img_url
            # print(img_url)
            try:
                pic = requests.Session().get(img_url, timeout=30)
                with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
                          "wb") as f:
                    f.write(pic.content)
                    f.close()
            except:
                with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    f.write(email + " : " + img_url + "\n\n")
                    f.close()
    browser.quit()
    time.sleep(random.choice(range(2,5)))


get_info("https://mechanical-engineering.uark.edu/Directory/index.php",
         "Department of Mechanical Engineering ",
         "University of Arkansas—Fayetteville")


get_info("https://first-year-engineering.uark.edu/directory.php",
         "First-Year Engineering Program",
         "University of Arkansas—Fayetteville")


get_info("https://bio-ag-engineering.uark.edu/directory/index.php",
         "Department of Biological & Agricultural Engineering",
         "University of Arkansas—Fayetteville")


get_info("https://biomedical-engineering.uark.edu/directory/index.php",
         "Department of Biomedical Engineering",
         "University of Arkansas—Fayetteville")


get_info("https://chemical-engineering.uark.edu/directory/index.php",
         "Department of Chemical Engineering",
         "University of Arkansas—Fayetteville")


get_info("https://civil-engineering.uark.edu/directory/index.php",
         "Department of Civil Engineering",
         "University of Arkansas—Fayetteville")


get_info("https://computer-science-and-computer-engineering.uark.edu/directory/index.php",
         "Department of Computer Science and Computer Engineering",
         "University of Arkansas—Fayetteville")


get_info("https://electrical-engineering.uark.edu/directory/index.php",
         "Department of Electrical Engineering",
         "University of Arkansas—Fayetteville")


get_info("https://industrial-engineering.uark.edu/directory/index.php",
         "Department of Industrial Engineering",
         "University of Arkansas—Fayetteville")