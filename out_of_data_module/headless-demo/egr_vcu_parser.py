# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: egr_vcu_parser.py

@time: 12/9/18 16:13


'''
from selenium.webdriver.chrome.options import Options

from utils.connection import *
import time
from db.operateSql import People
from db.operateSql import connect_db
from selenium import webdriver
from utils.selenuim_parser import SelenuimParser


db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, major, org="Virginia Commonwealth University"):
    global img_url
    browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=1))
    # chrome_options = Options()
    # prefs = {
    #             'profile.default_content_setting_values': {
    #         'images': 2,
    #         'javascript': 1
    #             }
    # }
    # chrome_options.add_experimental_option('prefs', prefs)
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    # browser = webdriver.Chrome()
    try:
        browser.get(url)
        # print(tmp)

    except Exception as e:
        print(e)
        browser.execute_script('window.stop()')

    finally:
        tmp = browser.find_elements_by_xpath('//div[@class="expert clearfix"]')
        # print(browser.page_source)

    for i in tmp:
        each = i.get_attribute('innerHTML')
        # print(each)
        img_url = extract("//img/@src", each)
        # print(img)
        web_url = extract("//h4/a/@href", each)
        name = extract("//h4/a/text()", each)
        if name:
            name = name.split(',')[0]
        else:
            continue
        email = extract("//a[contains(@href, '@')]/text()", each)
        print(name, email, major, web_url, img_url, org)
        user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)
        if img_url is not None and email is not None:
            # img = "http://be.utdallas.edu" + img_url
            # print(img_url)
            try:
                pic = requests.Session().get(img_url, timeout=300)

                with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
                          "wb") as f:
                    f.write(pic.content)
                    f.close()
            except Exception as e:
                print(e)
                print(img_url)
                with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    f.write(email + " : " + img_url + "\n")
                    f.close()
    browser.quit()
    time.sleep(3)


get_info("https://embed.expertfile.com/v1/organization/5500/1?font_family=Open%20Sans,%20Helvetica%20Neue,%20Helvetica&page_size=100&access=all&content=title,headline,phone,email&hide_search_bar=yes&hide_search_category=yes&hide_search_sort=yes&background_color=%23ffffff&url_color=%23fbb731&color=%23333333&category=Biomedical%20Engineering&tag=BME%20Faculty&url_override=http://egr.vcu.edu/directory/{{username}}/&open_tab=no&avatar=circle&powered_by=no",
         "Department of Biomedical Engineering")


get_info("https://embed.expertfile.com/v1/employee/5500/1?font_family=Open%20Sans,%20Helvetica%20Neue,%20Helvetica&page_size=10&access=all&content=title,headline,phone,email&hide_search_bar=yes&hide_search_category=yes&hide_search_sort=yes&url_color=%23ffb300&color=%23333333&category=Chemical%20and%20Life%20Science%20Engineering&tag=CLSE%20Tenured&url_override=http://egr.vcu.edu/directory/{{username}}/&open_tab=yes&avatar=circle&powered_by=no&channel=fe5e21e1-ea7c-41e0-be46-a20006760ab0&sort=name",
"Department of Chemical and Life Science Engineering")


get_info("https://embed.expertfile.com/v1/employee/5500/1?font_family=Open%20Sans,%20Helvetica%20Neue,%20Helvetica&page_size=100&access=all&content=title,headline,phone,email&hide_search_bar=no&hide_search_category=yes&hide_search_sort=yes&url_color=%23ffb300&color=%23333333&category=Computer%20Science&tag=CS%20Faculty&url_override=http://egr.vcu.edu/directory/{{username}}/&open_tab=yes&avatar=circle&powered_by=no&sort=name",
         "Department of Computer Science")


get_info("https://embed.expertfile.com/v1/organization/5500/1?font_family=Open%20Sans,%20Helvetica%20Neue,%20Helvetica&page_size=100&access=all&content=title,headline,phone,email&hide_search_bar=yes&hide_search_category=yes&hide_search_sort=yes&url_color=%23fbb731&color=%23333333&background_color=%23ffffff&url_override=http://egr.vcu.edu/directory/{{username}}/&category=all&tag=ECE%20Faculty&open_tab=no&avatar=circle&powered_by=no",
         "Department of Electrical & Computer Engineering")

get_info("https://embed.expertfile.com/v1/organization/5500/1?font_family=Open%20Sans,%20Helvetica%20Neue,%20Helvetica&page_size=100&access=all&content=title,headline,phone,email&hide_search_bar=yes&hide_search_category=yes&hide_search_sort=yes&background_color=%23ffffff&url_color=%23fbb731&color=%23333333&category=Mechanical%20and%20Nuclear%20Engineering&tag=MNE%20Faculty&url_override=http://egr.vcu.edu/directory/{{username}}/&open_tab=no&avatar=circle&powered_by=no",
         "Department of Mechanical & Nuclear Engineering")

