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

def SelenuimParse(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html_source = driver.page_source
    #driver.find_element_by_xpath("//[]").click()
    driver.find_element_by_xpath("//div[@class='author-group']/a[1]")
    #driver.close()
    return html_source

if __name__ == '__main__':
    url = ("http://www.sciencedirect.com/science/article/pii/S0267364916302151#!")
    driver = webdriver.Chrome()
    driver.get(url)
    html_source = driver.page_source
    
    # try:
    #     WebDriverWait(driver, 20).until(
    #         expected_conditions.presence_of_element_located((
    #             By.XPATH,"//div[@class='author-group']/a[1]"))
    #     ).click()
    # finally:
    #     driver.quit()
    
    driver.find_element_by_xpath("//div[@class='author-group']/a[1]").click()
    author = driver.find_element_by_xpath("//div[@class='author']/span[1]").text
    print(author)
    if "affiliation" in html_source:
        affiliation = driver.find_element_by_xpath("//div[@class='affiliation']").text
        print(affiliation)
    if "correspondence" in html_source:
        correspondence = driver.find_element_by_xpath("//div[@class='correspondence']").text
        print(correspondence)
    if "e-address" in html_source:
        email = driver.find_element_by_xpath("//div[@class='e-address']").text
        print(email)
    
