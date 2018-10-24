# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: ceas.py

@time: 2018/9/12 下午2:10


'''

from utils.connection import *
from utils.selenuim_parser import SelenuimParser
import time
from db.operateSql import People, connect_db
from selenium import webdriver
import re

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)

def getinfo(url):
    browser = webdriver.Chrome(chrome_options=SelenuimParser())
    browser.get(url)
    tmps = browser.find_elements_by_xpath("//tr[@role='row']")
    for each in tmps:
        res = each.get_attribute("innerHTML")
        # print(res)
        img_url = extract("//td[@class='sorting_1']/img/@src", res)
        if img_url == "fonts/nophoto.jpg":
            img_url = "https://www.ceas3.uc.edu/xml/fonts/nophoto.jpg"
        na = re.findall(r'target="_blank">(.*?)</a></b>', res)
        if na:
            name = na[0]
        else:
            continue
        web = re.findall(r'<b><a href="(.*?)" target="_blank">', res)
        if web:
            web_url = web[0]
        else:
            web_url = ""
        maj = re.findall(r'<br>Department of(.*?)<br><a href', res)
        if maj:
            major = "Department of" + maj[0]
        else:
            major = "College of Engineering and Applied Science"
        ema = re.findall(r'style="color:red">(.*?)</a>', res)
        if ema:
            email = ema[0]
        else:
            continue
        print(img_url, web_url, email, name, major)
        # user = People(email=email, name=name, major=major, web=web_url)
        # session.add(user)
        # try:
        #     session.commit()
        # except:
        #     session.rollback()
        time.sleep(1)
        if img_url is not None and email is not None:
            try:
                pic = requests.Session().get(img_url, timeout=30)
                with open("/Users/sunlei/scholar-private/out_of_data_module/lin_spider/pic/" + email + ".jpg",
                          "wb") as f:
                    f.write(pic.content)
                    f.close()
            except:
                with open("/Users/sunlei/scholar-private/out_of_data_module/lin_spider/error.txt", "a") as f:
                    f.write(email + " : " + img_url)
                    f.close()
        # browser.refresh()
    for i in range(0, 52):
        browser.find_element_by_xpath("//li[@id='courseList_next']/a").click()
        tmp = browser.find_elements_by_xpath("//tr[@role='row']")
        for each in tmp:
            res = each.get_attribute("innerHTML")
            # print(res)
            img_url = extract("//td[@class='sorting_1']/img/@src", res)
            if img_url == "fonts/nophoto.jpg":
                img_url = "https://www.ceas3.uc.edu/xml/fonts/nophoto.jpg"
            na = re.findall(r'target="_blank">(.*?)</a></b>', res)
            if na:
                name = na[0]
            else:
                continue
            web = re.findall(r'<b><a href="(.*?)" target="_blank">', res)
            if web:
                web_url = web[0]
            else:
                web_url = ""
            maj = re.findall(r'<br>Department of(.*?)<br><a href', res)
            if maj:
                major = "Department of" + maj[0]
            else:
                major = "College of Engineering and Applied Science"
            ema = re.findall(r'style="color:red">(.*?)</a>', res)
            if ema:
                email = ema[0]
            else:
                continue
            print(img_url, web_url, email, name, major)
            # user = People(email=email, name=name, major=major, web=web_url)
            # session.add(user)
            # try:
            #     session.commit()
            # except:
            #     session.rollback()
            time.sleep(1)
            if img_url is not None and email is not None:
                # img = "http://be.utdallas.edu" + img_url
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



getinfo("https://www.ceas3.uc.edu/xml/directory.php")