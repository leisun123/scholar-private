# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: cee_LSU_parser.py

@time: 2018/10/18 下午4:04


'''

from utils.connection import *
from db.operateSql import People, connect_db
import time

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def get_info(url, major):
    global img_url
    try:
        html = fetch(url)
        tmp = extract('//div[@class="col-md-12"]/p', html, True)
        # print(tmp)
    except:
        return get_info(url, major)

    for i in tmp:
        each = str(etree.tostring(i))
        img = extract("//a/img/@src", each)
        if not img:
            continue
        else:
            name = extract("//a/img/@alt", each).split(' photo')[0]
            img_url = "https://www.lsu.edu" + img
            web_url = "https://www.lsu.edu" + extract("//a/@href", each)
            try:
                source = fetch(web_url)
                email = extract("//a[contains(@href, '@')]/text()", source)
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
            except:
                print(name + "failed!")
                pass


get_info("https://www.lsu.edu/eng/cee/people/faculty-and-instructors.php", \
         "Department of Civil & Environmental Engineering")