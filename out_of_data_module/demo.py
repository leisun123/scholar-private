#coding:utf-8

import json
from utils.connection import *
import re
import traceback
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from ScholarConfig.config import USER_AGENT

def get(url):
    authorlist = []
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    print("succeed")
    lis = browser.find_elements_by_xpath('//span[@class="content"]')
    for i in lis:
        authordic = {}
        i.click()
        name =""
        email = ""
        aff = ""
        try:
            name = browser.find_element_by_xpath \
                       ("//div[@class='WorkspaceAuthor']/div/span[@class='text given-name']").text \
                   + " " + browser.find_element_by_xpath("//div[@class='WorkspaceAuthor']/div/span[@class='text surname']").text
        except:
            name = None
        try:
            email = browser.find_element_by_xpath("//div[@class='WorkspaceAuthor']/div[@class='e-address']").text
        except:
            email = None
        try:
            aff = browser.find_element_by_xpath("//div[@class='WorkspaceAuthor']/div[@class='affiliation']").text
        except:
            aff = None
        authordic.update({'name': name,
                          'email': email,
                          'affiliation': aff})
        authorlist.append(authordic)
    print(str(authorlist))
    print("----------------------------------------------------------\n")
# print(json_dict)


get("https://www.sciencedirect.com/science/article/pii/S2212671614000109")
get("https://www.sciencedirect.com/science/article/pii/S2212671614000134")



