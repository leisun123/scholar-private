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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def SelenuimParser(proxy_manager, user_agent, use_proxy):
    
    driver_option = webdriver.ChromeOptions()
    if use_proxy:
        driver_option.add_argument('--proxy-server={}'.format(use_proxy))
    driver_option.add_argument('--user-agent={}'.format(user_agent))
    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    pass
    # try:
    #     WebDriverWait(driver, 20).until(
    #         expected_conditions.presence_of_element_located((
    #             By.XPATH,"//div[@class='author-group']/a[1]"))
    #     ).click()
    # finally:
    #     driver.quit()

        
        
