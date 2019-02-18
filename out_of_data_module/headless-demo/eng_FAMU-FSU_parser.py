# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: eng_FAMU-FSU_parser.py

@time: 11/19/18 10:50 AM


'''


from utils.connection import *
import random
from db.operateSql import People, connect_db
from selenium.webdriver.chrome.options import Options
import time
from utils.selenuim_parser import SelenuimParser
from selenium import webdriver
import re

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)

major_list = [
    "Chemical & Biomedical Engineering",
    "Civil & Environmental Engineering",
    "Electrical & Computer Engineering",
    "Industrial & Manufacturing Engineering",
    "Mechanical Engineering"
]


def get_info(url, org="Florida A&M University - Florida State University"):
    browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=2))
    # browser = webdriver.Chrome()
    try:
        browser.get(url)
    except:
        browser.execute_script('window.stop()')
    finally:
        tmp = browser.find_elements_by_xpath("//div[contains(@class, 'col-xs-6 col-sm-4 col-md-3 col-lg-2 views-col')]")
        # print(tmp)
        for each in tmp:
            res = each.get_attribute('innerHTML')
            # print(res)
            web_url = extract("//div[@class='bio-photo']/div/a/@href", res)
            # print(web_url)
            if web_url:
                web = "https://eng.famu.fsu.edu" + web_url
            else:
                continue
            major = extract("//div[@class='views-field views-field-field-department-s-']/div/text()", res)
            print(major)
            if major not in major_list:
                continue
            img_url = extract("//div[@class='bio-photo']/div/a/img/@src", res)
            if not img_url:
                name = extract("//h4[@class='views-field views-field-title faculty-name'/]span/a/text()", res).split(',')[0]
            else:
                name = extract("//div[@class='bio-photo']/div/a/img/@title", res).split(',')[0]
            try:
                text = fetch(web)
                email = extract('//div[contains(text(), "@")]/text()', text)
                if not email:
                    continue
                print(email, name, web, major, org)
                user = People(email=email, name=name, major=major, web=web, orginazation=org)
                session.add(user)
                try:
                    session.commit()
                except Exception as e:
                    print(e)
                    session.rollback()
                time.sleep(random.choice(range(0, 3)))
                if img_url is not None and email is not None:
                    img = "https://eng.famu.fsu.edu" + img_url
                    print(img)
                    try:
                        pic = requests.Session().get(img, timeout=30)
                        with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
                                  "wb") as f:
                            f.write(pic.content)
                            f.close()
                    except:
                        with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                            f.write(email + " : " + img_url + "\n\n")
                            f.close()
            except Exception as e:
                print(e)
                pass
        browser.quit()


get_info(url="https://eng.famu.fsu.edu/directory")