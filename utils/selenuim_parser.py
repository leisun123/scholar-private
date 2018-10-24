#coding:utf-8
"""
@file:      webdriver
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/30 2:36
@description:
            --
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ScholarConfig.config import USER_AGENT


# class ChormeHeadless:
#     def __init__(self, driver=None):
#         self.driver = driver
#
#     def get_text(self, url, use_proxy=False):
#         chrome_options = Options()
#         user_agent = USER_AGENT
#         if use_proxy:
#             chrome_options.add_argument('--proxy-server={}'.format(use_proxy))
#         chrome_options.add_argument('user-agent={}'.format(user_agent))
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('lang=zh_CN.UTF-8')
#         prefs = {
#             'profile.default_content_setting_values': {
#                 'images': 2,
#                 'javascript': 2
#             }
#         }
#         chrome_options.add_experimental_option('prefs', prefs)
#         self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         self.driver.get(url)
#         self.driver.quit()
#         return self.driver.page_source
#
#     def get_screenshot(self, url, filepath, use_proxy=False):
#         chrome_options = Options()
#         user_agent = USER_AGENT
#         if use_proxy:
#             chrome_options.add_argument('--proxy-server={}'.format(use_proxy))
#         chrome_options.add_argument('user-agent={}'.format(user_agent))
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('lang=zh_CN.UTF-8')
#         self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         self.driver.get(url)
#         self.driver.save_screenshot(filepath)
#         self.driver.quit()



def SelenuimParser(use_proxy=False,
                   stopjs=1,
                   stopimage=1):
    chrome_options = Options()
    user_agent=USER_AGENT
    if use_proxy:
        chrome_options.add_argument('--proxy-server={}'.format(use_proxy))
    chrome_options.add_argument('user-agent={}'.format(user_agent))
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    prefs = {
        'profile.default_content_setting_values': {
            'images': stopimage,
            'javascript': stopjs
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)
    return chrome_options


# chrome = ChormeHeadless()
# chrome.get_text(url="https://www.baidu.com")
# if __name__ == '__main__':
#    driver = webdriver.Chrome()
#    driver.get("http://eng.auburn.edu/aero/faculty/")
#    html_source = (driver.page_source)
#    print(html_source)
#    from utils.connection import *
#    email = extract("//p[contains(text(),'@')]/./text()", html_source)
#    print(email)
#    import re
#    regex = r"([\w\.\-]+@[\w\.\-]+)"
#
#
#    print("-------------------------------------------")
#    email = re.search(regex, html_source).group()
#    print(email)
#