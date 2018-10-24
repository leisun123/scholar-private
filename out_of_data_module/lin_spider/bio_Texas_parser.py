# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: bio_Texas_parser.py

@time: 2018/7/18 上午9:23


'''

import requests
from utils.connection import *
import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException




url = "http://be.utdallas.edu/bioengineering/people/faculty/"


def get(url):
    browser = webdriver.Chrome()
    # browser = webdriver.PhantomJS()
    try:
        browser.get(url)
    except TimeoutException as e:
        browser.execute_script('window.stop()')
        print(e)
    finally:
        res = browser.find_elements_by_xpath("//div[@class='clearfix']")

        for each in res:
            res = each.get_attribute("innerHTML")
            # print(type(res))
            # print(res)
            major = "Department of Bioengineering"
            name = extract("//div[@class='col-25']/img/@alt", res)
            web_url = extract("//strong[@class='larger']/a/@href", res)
            if web_url is None:
                web = ""
            else:
                web = "http://be.utdallas.edu" + web_url
            email = extract("//div[@class='col-75']/p[1]/a/text()", res)
            img_url = extract("//div[@class='col-25']/img/@src", res)
            # name = each.find_element_by_xpath("//div[@class='col-25']/img").get_attribute("alt")
            # web_url = each.find_element_by_xpath("//strong[@class='larger']/a").get_attribute("href")
            # if web_url is None:
            #     web = ""
            # else:
            #     web = "http://be.utdallas.edu" + web_url
            # email = each.find_element_by_xpath("//div[@class='col-75']/p[1]/a").text
            # img_url = each.find_element_by_xpath("//div[@class='col-25']/img").get_attribute("src")
            print(name, " ", email, " ", major, " ", web, " ", img_url)

            # if img_url is not None and email is not None:
            #     img = "http://be.utdallas.edu" + img_url
            #     try:
            #         pic = requests.Session().get(img, timeout=30)
            #         with open("/Users/sunlei/scholar-private/out_of_data_module/lin_spider/pic/" + email + ".jpg", "wb") as f:
            #             f.write(pic.content)
            #             f.close()
            #     except:
            #         with open("/Users/sunlei/scholar-private/out_of_data_module/lin_spider/error.txt" ,"a") as f:
            #             f.write(email + " : " + img_url)
            #             f.close()
            # data = [name, email, major, web]
            # with open("/Users/sunlei/scholar-private/out_of_data_module/lin_spider/scholar.csv", "a") as f:
            #     writer = csv.writer(f)
            #     writer.writerow(data)
            #     f.close()


get(url)
get("http://be.utdallas.edu/bioengineering/people/affiliated-faculty/")