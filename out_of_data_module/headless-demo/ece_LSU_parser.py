# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: ece_LSU_parser.py

@time: 2018/10/18 下午5:09


'''

from utils.connection import *
from db.operateSql import People, connect_db
from utils.selenuim_parser import SelenuimParser
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException


db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, major):
    global img_url
    try:
        html = fetch(url)
        tmp = extract('//table[@id="scholarships"]/tbody/tr', html, True)
        # print(tmp)
    except:
        return get_info(url, major)

    for i in tmp:
        each = str(etree.tostring(i))
        web = extract("//a/@href", each)
        if web:
            web_url = "https://www.lsu.edu/" + web
            try:

                browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2))
                browser.get(web_url)
                browser.set_page_load_timeout(3)

            except TimeoutException as e:
                print(e)
                browser.execute_script('window.stop()')
            finally:
                # source = str(etree.tostring(browser.page_source))
                source = browser.page_source
                # print(source)
                email = extract("//a[contains(@href, '@')]/text()", source)
                # print(email)
                name = extract("//h1[@class='fac-name']/text()", source)
                img_url = extract("//div[@class='fac-photo']/img/@src", source)
                print(name, email, major, web_url, img_url)
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
                browser.quit()
        else:
            continue


get_info("https://www.lsu.edu/eng/ece/people/index.php", \
         "Division of Electrical & Computer Engineering")