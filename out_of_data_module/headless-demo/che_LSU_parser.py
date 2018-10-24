# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: che_LSU_parser.py

@time: 2018/10/18 下午4:43


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
        tmp = extract('//div[@class="col-md-9"]/div[@class="col-md-3"]', html, True)
        # print(tmp)
    except:
        return get_info(url, major)

    for i in tmp:
        each = str(etree.tostring(i))
        web = extract("//p/a[1]/@href", each)
        if web:
            name = extract("//p/a[1]/@title", each)
            web_url = "https://www.lsu.edu" + web
            img = extract("//img/@src", each)
            if img:
                img_url = "https://www.lsu.edu" + img
            try:
                source = fetch(web_url)
                email = extract("//a[contains(@href, '@')]/text()", source)
                if not email:
                    continue
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
                    # print(img_url)
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
                print(name + "Failed")
                pass
        else:
            continue



get_info("https://www.lsu.edu/eng/che/people/faculty.php", \
         "Cain Department of Chemical Engineering")