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

def SelenuimParse(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html_source = driver.page_source
    #driver.find_element_by_xpath("//[]").click()
    driver.quit()
    return html_source

if __name__ == '__main__':
    html=(SelenuimParse("http://www.sciencedirect.com/science/article/pii/S0020025515006581"))
    from Tool import extract
    a=extract("//a[@class='cye-lm-tag']/a/@href",html)
    print(html)

