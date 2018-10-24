# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: mse_uta_parser.py

@time: 2018/8/9 上午11:29


'''

import requests
from utils.connection import *
import time
from db.operateSql import People, connect_db
import re

db_url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(db_url)


def getInfo(url, major):
    try:
        res = fetch(url)
    except:
        return getInfo(url, major)
    tmp = extract("//div[@class='faculty-directory']/p", res, True)


    for each in tmp:
        source = str(etree.tostring(each))

        # print(source)
        url = extract("//strong/img/@src", source)
        # print(url)
        if url is not None:
            pic_url = "http://www.uta.edu/mse/" + url.split("./")[-1]
        else:
            pic_url = ""
        email = re.search(r'<br/> <a href="(.*?)">', source, re.S)
        if email is not None:
            email = str(email).split(':')[-1].split('"')[0]
        else:
            continue
        name = extract("//strong/img/@alt", source)
        if name:
            name = str(name).split('Dr. ')[-1]
        else:
            continue
        web_url = re.findall(r'\| <a href="(.*?)">', source, re.S)
        if web_url:
            web = str(web_url[0])
        else:
            web = ""
        print(pic_url, " ", name, " ", email, " ", web, " ", major)
        try:
            pic = requests.Session().get(pic_url, timeout=30)
            with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg", "wb") as f:
                f.write(pic.content)
                f.close()
        except:
            with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
                f.write(email + " : " + pic_url + "\n")
        user = People(email=email, name=name, major=major, web=web)
        session.add(user)
        try:
            session.commit()
        except:
            session.rollback()
        time.sleep(1)


getInfo("http://www.uta.edu/mse/faculty-directory.php", \
        "Department of Materials Science and Engineering")