# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: cse_uta_parser.py

@time: 2018/8/23 上午9:36


'''

from utils.connection import *
# import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from db.operateSql import People, connect_db
import re
import base64
from PIL import Image

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get(url):
    browser = webdriver.Chrome()
    try:
        browser.get(url)
    except TimeoutException as e:
        browser.execute_script('window.stop()')
        print(e)
    finally:
        res = browser.find_elements_by_xpath("//div[@class='faculty-directory']/p")
        print(len(res))
        for each in res:
            source = each.get_attribute("innerHTML")

            major = "Department of Computer Science and Engineering"

            url = extract("//img/@src", source)
            email = extract("//*[contains(@href, '@')]/text()", source)
            if email is not None:
                email = str(email).split(':')[-1].split('"')[0]
            else:
                continue
            name = extract("//img/@alt", source)
            if name:
                pass
            else:
                continue
            web_url = re.findall(r'\| <a href="(.*?)">Website</a>', source, re.S)
            # print(web_url)
            if web_url:
                web = str(web_url[0])
            else:
                web = ""
            print(name, " ", email, " ", web, " ", major)
            #
            if url is not None and email is not None:
                url = url.split(",")[-1]
                try:
                    # pic = requests.Session().get(url, timeout=30)
                    pic = base64.b64decode(url)
                    with open("/Users/sunlei/scholar-private/out_of_data_module/test/" + email + ".jpg", "wb") as f:
                        f.write(pic)
                        f.close()
                except:
                    # with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    #     f.write(email + " : " + url + "\n\n")
                    #     f.close()
                    pass
                # user = People(email=email, name=name, major=major, web=web)
                # session.add(user)
                # try:
                #     session.commit()
                # except:
                #     session.rollback()
                # time.sleep(1)


get("https://cse.uta.edu/faculty-directory-list.php")