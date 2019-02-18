#coding:utf-8

from utils.connection import *
import time
from db.operateSql import People
from db.operateSql import connect_db
from selenium import webdriver
from utils.selenuim_parser import SelenuimParser


db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, org="West Virginia University (Statler)"):
    global img_url
    try:
        # html = fetch(url)
        # tmp = extract('//ul[@class="directory"]/li', html, True)
        # browser = webdriver.Chrome()
        browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=2))
        browser.get(url)
        tmp = browser.find_elements_by_xpath('//ul[@class="directory"]/li')
        print(tmp)
    except Exception as e:
        print(e)
        return get_info(url)

    for i in tmp:
        # each = str(etree.tostring(i))
        each = i.get_attribute('innerHTML')
        # print(each)
        img = extract("//div[@class='directory__individual-photo']/img/@src", each)
        # print(img)

        if not img:
            img_url = ""
        else:
            img_url = "https://www.statler.wvu.edu" + img
            # name = extract("//h2[@class='wvu-profile__name']/a/text()", each)
            web_url = extract("//h2[@class='wvu-profile__name']/a/@href", each)
            # print(web_url)
            try:
                bro = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=2))
                bro.get(web_url)
                source = bro.page_source
                email = extract("//a[contains(@href, '@')]/text()", source)
                # name = extract("//div[@class='col-sm-8']/h1/text()", source).split(',')[0]
                # major = extract("//h2[@class='wvu-profile__job-title wvu-h3']/text()", source)
                # if major:
                #     major = major.split(' - ')[1]
                # else:
                #     major = ""
                # print(name, email, major, web_url, img_url, org)
                # user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
                # session.add(user)
                # try:
                #     session.commit()
                # except:
                #     session.rollback()
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
                bro.quit()
            except Exception as e:
                print(web_url)
                print(e)
                pass
    browser.quit()


get_info("https://www.statler.wvu.edu/faculty-staff/faculty")
