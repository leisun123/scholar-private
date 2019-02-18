# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: withdraw_data.py

@time: 2018/7/18 上午8:12


'''

from db.operateSql import connect_db
import csv
from sqlalchemy import select
from db.operateSql import People

url = "mysql+pymysql://root:123456@localhost/sc"
session = connect_db(url)

datas = session.query(People.name, People.email, People.major, People.web, People.orginazation).all()

with open('new2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'email', 'major', 'web', 'organization'])
    for row in datas:
        writer.writerow(row)