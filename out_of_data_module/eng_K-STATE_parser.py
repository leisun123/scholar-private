# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: eng_K-STATE_parser.py

@time: 11/19/18 2:18 PM


'''


from utils.connection import *
import time
from db.operateSql import People, connect_db

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url, frontstr, org="Kansas State University"):
    try:
        res = fetch(url)
    except:
        return getInfo(url, frontstr, org)
    tmp = extract("//tbody/tr/td", res, True)
    # print(tmp)
    major = extract("//div[@id='ksu-unitbar']/h2/a/text()", res)

    for each in tmp:
        source = str(etree.tostring(each))

        # print(source)
        email = extract("//a[contains(@href, '@')]/text()", source)
        if not email:
            continue
        name = extract("//strong/text()", source)
        if not name:
            name = extract("//strong/a/span/text()", source)
        web_url = extract("//a[contains(@href, '/people')]/@href", source)
        # print(web_url)
        img_url = ""
        if web_url:
            web_url= frontstr + web_url
            try:
                text = fetch(web_url)
                img_url = extract("//img[contains(@src, '/docs/people')]/@src", text)
            except:
                pass
        else:
            continue
        print(frontstr+str(img_url), " ", name, " ", email, " ", web_url, " ", major, " ", org)
        if img_url:
            try:
                img_url = frontstr + img_url
                pic = requests.Session().get(img_url, timeout=30)
                with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg", "wb") as f:
                    f.write(pic.content)
                    f.close()
            except:
                with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                    f.write(email + " : " + img_url + "\n")
        user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)


getInfo("http://www.ece.k-state.edu/people/faculty/index.html", "http://www.ece.k-state.edu")
