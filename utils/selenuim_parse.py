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

# def SelenuimParse(url):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     html_source = driver.page_source
#     #driver.find_element_by_xpath("//[]").click()
#     driver.find_element_by_xpath("//div[@class='author-group']/a[1]")
#     #driver.close()
#     return html_source

if __name__ == '__main__':
    from utils.connection import *
    driver = webdriver.Chrome()
    driver.get("http://www.sciencedirect.com/science/journal/17427061?sdc=1")
    html=driver.page_source
    driver.quit()
    item_url = extract("//a[@class='cLink artTitle S_C_artTitle ']/@href",html,multi=True)
    print(item_url)
    for url in item_url:
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

        major = None
        university = None
        author_list = driver.find_elements_by_xpath("//div[@class='author-group']/a")
        for i in author_list:
            try:
                print(i)
                i.click()
                email = driver.find_element_by_xpath("//div[@class='e-address']").text
                print("email: ", email.replace('Opens the author workspace','').strip())
                
                firstname = driver.find_element_by_xpath("//div[@class='author']/span[1]").text
                print(firstname)
        
                lastname = driver.find_element_by_xpath("//div[@class='author']/span[2]").text
                print(lastname)
                

                
                try:
                     affiliation = driver.find_element_by_xpath("//div[@class='affiliation']").text
                     major = affiliation.split(',')[0].replace('Corresponding authors at:','').\
                         replace('Opens the author workspace','').\
                         replace('Corresponding author.','').\
                         replace('Corresponding author at:','').\
                         strip()
                     for i in affiliation.split(','):
                         if 'University' in i:
                             university = i.replace('Corresponding author at:','').strip()
    
                except:
                     pass
        
        
                try:
                     correspondence = driver.find_element_by_xpath("//div[@class='correspondence']").text
                     major = affiliation.split(',')[0].replace('Corresponding authors at:','').\
                         replace('Opens the author workspace','').\
                         replace('Corresponding author.','').\
                         replace('Corresponding author at:','').\
                         strip()
                     for i in affiliation.split(','):
                         if 'university' in i:
                             university = i.replace('Corresponding author at:','').strip()
                except:
                     pass
                print("major: ",major)
                print("university:",university)
            except:
                pass
            print("\n")
        driver.quit()
        
        
