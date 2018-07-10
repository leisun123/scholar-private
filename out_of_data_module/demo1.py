# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: demo1.py

@time: 2018/6/27 下午6:09


'''

from selenium import webdriver
import json
import xlwt

book = xlwt.Workbook(encoding="UTF-8")
sheet = book.add_sheet("data")
sheet.write(0, 0, "ID")
sheet.write(0, 1, "coord")
sheet.write(0, 2, "name")
sheet.write(0, 3, "type")
book.save("/Users/sunlei/scholar/out_of_data_module/data.xls")

browser = webdriver.Chrome()
browser.get("https://flightaware.com/ajax/ignoreall/trackpoll.rvt?token=c35ca45ecbca57cd1ea443d1c65c36426ea06630de026ffd737977e4a40a26ead614b3f2ddde9907453c214a859f7965-88dd7c1a0d41355d480f52fc6e8214b08d5ec890688340e3-248f57a8de48cfedb6ab0e99c2552160fdf72ca1&locale=zh_CN&summary=0")
res = browser.find_element_by_xpath("//pre").text

req = json.loads(res)

info = req.get("flights")
print(type(info))

c = 1

data = {}
for i in info:
    txt = info[i]
    print(txt["destination"].get("coord"), txt["destination"].get("friendlyName"))
    print(txt["origin"].get("coord"), txt["origin"].get("friendName"))
    sheet.write(c, 0, str(i))
    sheet.write(c, 1, str(txt["destination"].get("coord")))
    sheet.write(c, 2, str(txt["destination"].get("friendlyName")))
    sheet.write(c, 3, "destnation")
    book.save("/Users/sunlei/scholar/out_of_data_module/data.xls")

    c = c + 1

    sheet.write(c, 0, str(i))
    sheet.write(c, 1, str(txt["origin"].get("coord")))
    sheet.write(c, 2, str(txt["origin"].get("friendlyName")))
    sheet.write(c, 3, "origin")
    book.save("/Users/sunlei/scholar/out_of_data_module/data.xls")

    c = c + 1
