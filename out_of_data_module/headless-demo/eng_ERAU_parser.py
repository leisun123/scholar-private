# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: eng_ERAU_parser.py

@time: 11/9/18 5:19 PM


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

def get_info(url, major, org="Embry-Riddle Aeronautical University"):
    browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=1))
    try:
        browser.get(url)
    except:
        browser.execute_script('window.stop()')
    finally:
        tmp = browser.find_elements_by_class_name('media')
        # print(tmp)
        for each in tmp:
            res = each.get_attribute('innerHTML')
            # print(res)
            img_url = extract("//img[@class='media-object']/@src", res)
            if not img_url:
                name = extract("//h4[@class='media-heading name']/text()", res)
            else:
                name = extract("//img[@class='media-object']/@alt", res)
            web = ""
            id = extract('//div/a[@data-toggle="modal"]/@data-faculty-uid', res)
            if id:
                js_url = 'https://webforms.erau.edu/common/services/peoplesearch/faculty.cfc?callback=jQuery1113072479908569549_1541990949502&method=getFacultyByUid&returnformat=plain&uidList=' + id
                try:
                    text = fetch(js_url)
                    email = re.findall(r'"EMAIL":"(.*?)",', text, re.S)[0]
                    print(email, name, web, img_url, major, org)
                    user = People(email=email, name=name, major=major, web=web, orginazation=org)
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
                except Exception as e:
                    print(e)
                    pass
            else:
                continue
        browser.quit()
        time.sleep(random.choice(range(2, 5)))


get_info("https://daytonabeach.erau.edu/college-engineering/aerospace/faculty/", "Department of Aerospace Engineering")
get_info("https://daytonabeach.erau.edu/college-engineering/civil/faculty/", "Department of Civil Engineering")
get_info("https://daytonabeach.erau.edu/college-engineering/electrical-computer-software-systems/faculty/", "Department of Electrical, Computer, Software, and Systems Engineering")
get_info("https://daytonabeach.erau.edu/college-engineering/fundamentals/faculty/", "Department of Engineering Fundamentals")
get_info("https://daytonabeach.erau.edu/college-engineering/mechanical/faculty/", "Department of Mechanical Engineering")