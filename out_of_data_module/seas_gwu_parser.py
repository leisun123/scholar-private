# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: seas_gwu_parser.py

@time: 2018/8/23 上午11:21


'''

from utils.connection import *
import time
from db.operateSql import People, connect_db
from selenium import webdriver

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url):
    try:
        res = fetch(url)
    except:
        return getInfo(url)
    tmp = extract("//div[@class='letter a-z-basic']/ul/li", res, True)
    print(len(tmp))


    for each in tmp:
        source = str(etree.tostring(each))
        web = extract("//a/@href", source)
        if web:
            web = "https://www.seas.gwu.edu/" + web
            # print(web)
            browser = webdriver.PhantomJS()
            # browser = webdriver.Chrome()
            browser.get(web)
            # print(page_source)

            img_url = browser.find_element_by_xpath("//div[@class='person-image-wrapper']/img").get_attribute('src')
            # print(url)
            email = browser.find_element_by_xpath("//a[@property='email']").text
            if not email:
                continue
            firstname = browser.find_element_by_xpath("//span[@property='givenName']").text
            lastname = browser.find_element_by_xpath("//span[@property='familyName']").text
            # print(firstname)
            # print(lastname)
            if firstname and lastname:
                name = str(firstname) + str(lastname)
                # print(name)
            else:
                continue
            major = browser.find_element_by_xpath('//*[@id="breadcrumb"]/a[5]').text
            print(img_url, " ", name, " ", email, " ", web, " ", major)
            # try:
            #     pic = requests.Session().get(img_url, timeout=30)
            #     with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg", "wb") as f:
            #         f.write(pic.content)
            #         f.close()
            # except:
            #     with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
            #         f.write(email + " : " + img_url + "\n")
            # user = People(email=email, name=name, major=major, web=web)
            # session.add(user)
            # try:
            #     session.commit()
            # except:
            #     session.rollback()
            # time.sleep(1)
        else:
            continue


getInfo("https://www.seas.gwu.edu/faculty-directory")