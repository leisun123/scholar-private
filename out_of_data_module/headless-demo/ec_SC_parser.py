# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: ec_SC_parser.py

@time: 11/2/18 11:59 AM


'''

from utils.connection import *
from db.operateSql import People, connect_db
from selenium.webdriver.chrome.options import Options
import time
from utils.selenuim_parser import SelenuimParser
from selenium import webdriver

# db_url = "mysql+pymysql://root:123456@localhost/sc"
# session = connect_db(db_url)
#
#
# def get_info(url, major, org):
#     global img_url
#     try:
#         html = fetch(url)
#         tmp = extract('//tbody/tr', html, True)
#         # print(tmp)
#     except:
#         return get_info(url, major, org)
#
#     for i in tmp:
#         source = str(etree.tostring(i))
#         # print(source)
#         email = extract("//td/a[contains(@href, '@')]/text()", source)
#         title = extract("//td[3]/text()", source)
#         if "Adjunct" in title:
#             continue
#         if not email:
#             continue
#         web = extract("//td/a[contains(@href, '/study/colleges_schools/')]/@href", source)
#         fullname = extract("//td[2]/a/text()", source)
#         name = fullname.split(',')[-1] + fullname.split(',')[0]
#         if web:
#             web_url = "https://www.sc.edu" + web
#             # res = fetch(web_url)
#             # browser = webdriver.Chrome(chrome_options=SelenuimParser(stopimage=2, stopjs=2))
#
#             chrome_options = Options()
#             prefs = {
#                 'profile.default_content_setting_values': {
#                     'images': 2,
#                     'javascript': 2
#                 }
#             }
#             chrome_options.add_experimental_option('prefs', prefs)
#             # chrome_options.add_argument('--headless')
#             browser = webdriver.Chrome(chrome_options=chrome_options)
#             browser.get(web_url)
#             # browser.set_page_load_timeout(3)
#             res = browser.page_source
#             img = extract("//img[@class='max-image']/@src", res)
#             if img:
#                 img_url = "https://www.sc.edu" + img
#                 # print(img_url)
#             else:
#                 img_url = ""
#             browser.quit()
#             print(name, email, major, web_url, img_url, org)
#             user = People(email=email, name=name, major=major, web=web_url, orginazation=org)
#             session.add(user)
#             try:
#                 session.commit()
#             except:
#                 session.rollback()
#             time.sleep(1)
#             if img_url is not None and email is not None:
#                 # img = "http://be.utdallas.edu" + img_url
#                 # print(img_url)
#                 try:
#                     pic = requests.Session().get(img_url, timeout=30)
#                     with open("/Users/sunlei/scholar-private/out_of_data_module/pic/" + email + ".jpg",
#                               "wb") as f:
#                         f.write(pic.content)
#                         f.close()
#                 except:
#                     with open("/Users/sunlei/scholar-private/out_of_data_module/timeout.txt", "a") as f:
#                         f.write(email + " : " + img_url)
#                         f.close()
#
#
# get_info("https://www.sc.edu/study/colleges_schools/engineering_and_computing/faculty-staff/index.php", \
#          "College of Engineering and Computing", \
#          "University of South Carolina")
chrome_options = Options()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'javascript': 2
    }
}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("http://louisville.edu/speed/people/faculty")
