# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: engr_ohio_parser.py

@time: 1/7/19 14:56


'''


from db.operateSql import *
from utils.connection import *
import random


depts = [
    "Aviation",
    "Chemical and Biomolecular Engineering",
    "Civil Engineering",
    "Engineering Technology and Management",
    "Electrical Engineering and Computer Science",
    "Industrial and Systems Engineering",
    "Mechanical Engineering"
]

def get_info(url, org="Ohio University (Russ)"):
    try:
        html = fetch(url)
        tmp = extract("//div[@class='group']", html, True)

        info = {}
        for i in tmp:
            each = str(etree.tostring(i))
            dept = extract("//h3/a[1]/text()", each)
            # print(dept)
            if dept in depts:
                # print(dept)
                dic = {}
                urls = extract("//a[contains(@href, 'profiles.cfm')]/@href", each, True)
                dic[dept] = urls
                info.update(dic)

        # print(info)

        for each in depts:
            for url in info.get(each):
                major = "Department of " + each
                web_url = "https://www.ohio.edu/engineering/about/people/" + url
                try:
                    res = fetch(web_url)
                    name = extract("//h3[@class='First_Name']/span[1]/text()", res) + " " +\
                           extract("//h3[@class='First_Name']/span[2]/text()", res)
                    email = extract("//div[@class='contactInfo col']//a[contains(@href, '@')]/text()", res)
                    img = extract("//span[@class='eng_Image']/img/@src", res)
                    if img:
                        img_url = "https://www.ohio.edu" + img
                    else:
                        img_url = ""
                    print(name, email, major, web_url, img_url, org)
                    save_info(name=name, email=email, web_url=web_url, img_url=img_url, org=org, major=major)

                except Exception as e:
                    print(e)
                    print(web_url)
                    continue

            time.sleep(random.choice(range(1, 5)))

    except Exception as e:
        print(e)
        return get_info(url)


get_info("https://www.ohio.edu/engineering/about/people/departmental-listing.cfm")