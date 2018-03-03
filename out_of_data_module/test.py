from utils.connection import *
import requests
import json
from threadpool import *
import time
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
import re

def getArticleInfo(i):#获取所有文章的信息
    infoList =[]
    new = {}
    url = "https://www.sciencedirect.com" + i
    try:
        keywords = ""
        author = ""
        pdfurl = ""
        html = fetch(url)
        title = extract("//span[@class='title-text']/text()", html, False)
        if str(title) == "None":
            title = "No Found"
        keyword = extract("//div[@class='keywords']/span/text()", html, True)
        if keyword:
            for key in keyword:
                keywords = keywords + key + ";"
        else:
            keywords = "No Found"
        author_group = extract("//a[@class='author size-m workspace-trigger']", html, True)
        if author_group:
            for auth in author_group:
                firstname = extract("//span[@class='text given-name']/text()", str(etree.tostring(auth)), False)
                lastname = extract("//span[@class='text surname']/text()", str(etree.tostring(auth)), False)
                name = str(firstname) + " " + str(lastname)
                author = author + name + ";"
        else:
            author = "No Found"
        a = extract("//a[@class='anchor PdfDownloadButton']/@href", html, False)
        if a is None:
            b = re.findall(r'"linkToPdf":"(.*?)"},"',html)[0]
            pdfurl = "https://www.sciencedirect.com" + b
        else:
            pdfurl = "https://www.sciencedirect.com" + a
        if pdfurl == "https://www.sciencedirect.com":
            pdfurl = "No Found"
        time = extract("//span[@class='size-m']/text()[2]", html, False)
        if time == "" or time is None:
            time = "No Found"
        issue = extract("//a[@class='publication-title-link']/text()", html, False)
        if issue == "" or issue is None:
            issue = "No Found"
        new.update({"title": title, "keywords": keywords, "author": author, "issue": issue, "pdf": pdfurl, "time": time})
    except Exception as e:
        print(e)
        print(url)
        with open("./TODO.txt","a") as f:
            f.write(url + "\n")
            f.close()
    try:
        # sqlinput(new)
        print(new)
    except Exception as e:
        print(e)
        pass
    return infoList

def sqlinput(infodic):
    with SSHTunnelForwarder(
    ('39.104.50.183',22),
    ssh_username = "sc",
    ssh_pkey="./id_rsa",
    remote_bind_address=('127.0.0.1',5432)
    ) as server:
        server.start()
        print("successfully connected")
        engine = create_engine('postgresql://wyn:weiaizq1314@127.0.0.1:{}/sc_2018'.format(server.local_bind_port))
        Session = sessionmaker(bind=engine)
        session = Session()
        print("Database session created")
        tit = str(infodic['title'])
        keyw = str(infodic['keywords'])
        aut = str(infodic['author'])
        iss = str(infodic['issue'])
        tim = str(infodic['time'])
        pd = str(infodic['pdf'])
        # print(tit,keyw,aut,iss,tim,pd)
        sql = '''INSERT INTO paper(title,keywords,author,issue,pdf,"time",findtime) VALUES {}'''.format((tit,keyw,aut,iss,pd,tim,time.strftime('%Y:%m:%d:%M:%S', time.localtime(time.time()))))
        session.execute(sql)
        session.commit()
        server.stop()



with open('./url.txt') as f:
    line = f.readline()
    while line:
        getArticleInfo(line)
        line = f.readline()
        time.sleep(3)

# server = SSHTunnelForwarder(
#     ('39.104.50.183', 22),  # Remote server IP and SSH port
#     ssh_username="sc",
#     ssh_pkey='./id_rsa',
#     remote_bind_address=('localhost', 5432)
# )
#
# server.start()  # start ssh sever
#
# # connect to PostgreSQL
# engine = create_engine('postgresql://wyn:weiaizq1314@127.0.0.1:{}/sc_2018'.format(server.local_bind_port))
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # test data retrieval
# test = session.execute('''INSERT INTO paper(title,keywords,author,issue,pdf,"time",findtime) VALUES {}'''.format((str("aa"),str("bb"),str("cc"),str("dd"),str("ee"),str("ff"),str("gg"))))
# session.commit()
# server.stop()
print(random.uniform(1,4))