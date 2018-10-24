# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: purdue_parser.py

@time: 2018/9/17 下午8:49


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
        tmp = extract("//div[@class='people-text']/h4/a/@href", html, True)
    except:
        return get_info(url, major)

    for each in tmp:
        if each:
            web_url = "http://www.engr.iupui.edu" + each
            res = fetch(web_url)
            img = extract("//div[@class='inset-right faculty-photo']/img/@src", res)
            if img:
                img_url = "http://www.engr.iupui.edu" + img
            name = extract("//div[@class='caption']/h5/text()", res)
            email = extract("//div[@class='caption']/p/text()[3]",res)
            if email:
                email = email.strip()
            else:
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



get_info("http://www.engr.iupui.edu/departments/me/people/faculty-and-staff.php",\
         "Department of Mechanical and Energy Engineering")


