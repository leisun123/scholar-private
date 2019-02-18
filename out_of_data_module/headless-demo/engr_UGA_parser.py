# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: engr_UGA_parser.py

@time: 11/24/18 16:17


'''

from utils.connection import *
from db.operateSql import People, connect_db
import time

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, org="University of Georgia"):
    global img_url
    try:
        html = fetch(url)
        tmp = extract('//div[@class="people-list"]/article', html, True)
        # print(tmp)
    except:
        return get_info(url)

    for i in tmp:
        each = str(etree.tostring(i))
        img = extract("//div[@class='photo']/@style", each)
        # print(img)
        if not img:
            img_url = ""
        else:
            # name = extract("//a/img/@alt", each).split(' photo')[0]
            img_url = img.split('url(')[1].split(');')[0]
            web_url = "http://www.engr.uga.edu" + extract("//a[@class='content']/@href", each)
            # print(web_url)
            try:
                source = fetch(web_url)
                email = extract("//a[contains(@href, '@')]/text()", source)
                name = extract("//div[@class='col-sm-8']/h1/text()", source).split(',')[0]
                major = extract("//ul[@class='categories']/li[1]/a/text()", source)
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
            except Exception as e:
                print(web_url)
                print(e)
                pass


get_info("http://www.engr.uga.edu/people/faculty")