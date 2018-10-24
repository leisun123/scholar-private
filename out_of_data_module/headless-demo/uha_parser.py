# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: uha_parser.py

@time: 2018/9/17 上午10:00


'''

from utils.connection import *
from selenium import webdriver
from db.operateSql import People, connect_db
import time

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url):
    global img_url, browser
    try:
        # res = fetch(url)
        browser = webdriver.Chrome()
        # print(res)
        browser.get(url)
    except Exception as e:
        browser.execute_script('window.stop()')
        print(e)
    finally:
        dean_tmp = browser.find_elements_by_xpath('//div[@class="row multi layout-staff"][1]/div[@class="col-sm-4"]')
        cue_tmp = browser.find_elements_by_xpath('//*[@id="articleBody"]/div[2]/div[@class="col-sm-4"]')
        cme_tmp = browser.find_elements_by_xpath('//*[@id="articleBody"]/div[3]/div[@class="col-sm-4"]')
        cee_tmp = browser.find_elements_by_xpath('//*[@id="articleBody"]/div[5]/div[@class="col-sm-4"]')
        ece_tmp = browser.find_elements_by_xpath('//*[@id="articleBody"]/div[7]/div[@class="col-sm-4"]')
        iseem_tmp = browser.find_elements_by_xpath('//*[@id="articleBody"]/div[9]/div[@class="col-sm-4"]')
        mae_tmp = browser.find_elements_by_xpath('//*[@id="articleBody"]/div[11]/div[@class="col-sm-4"]')
        info = {
            "Office of the Dean": dean_tmp,
            "Center for Undergraduate Engineering Education": cue_tmp,
            "Chemical & Materials Engineering Department": cme_tmp,
            "Civil & Environmental Engineering Department": cee_tmp,
            "Electrical & Computer Engineering Department": ece_tmp,
            "Industrial & Systems Engineering and Engineering Management Department": iseem_tmp,
            "Mechanical & Aerospace Engineering Department": mae_tmp
        }
    exception = ['Office of the Dean',
                 'Center for Undergraduate Engineering Education',
                 'Mechanical & Aerospace Engineering Department']
    for each in info.keys():
        for i in info[each]:
            # res = str(etree.tostring(i))
            res = i.get_attribute("innerHTML")
            # print(res)
            major = each
            web = extract("//a[contains(@href,'departments')]/@href", res)
            if web:
                if "https://" in web:
                    web_url = web
                else:
                    web_url = "https://www.uah.edu" + web
            else:
                web_url = ""
            img = extract("//div[@class='image-holder']/img/@src", res)
            if img:
                img_url = "https://www.uah.edu" + img
            name = extract("//div[@class='image-holder']/img/@alt", res)
            if not name:
                continue
            email = extract("//a[contains(@href,'@uah.edu')]/text()", res)
            if not email:
                continue
            print(name, " ", email, " ", web_url, " ", img_url, " ", major)
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

get_info("https://www.uah.edu/eng/faculty-staff")
