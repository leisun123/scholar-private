# #-*-coding:utf-8-*-
#
# from utils.connection import *
# from utils.set_value import *
#
# def get_data(url):
#     res = fetch(url)
#     tmp = extract("//div[@class='directory_entry']",res,multi=True)
#     for a in tmp:
#         name = extract("//*[@class='name']/b/text()",html_source=str(etree.tostring(a)))
#         email = extract("//*[@class='email']/text()",html_source=str(etree.tostring(a)))
#         web = extract("//a/@href", str(etree.tostring(a)))
#         avtar = extract("//a/img/@src",str(etree.tostring(a)))
#         organization = "University of North Carolina"
#         major = "Department of Chemical and Biomolecular Engineering"
#         print(set_value(name,email,web,organization,major,avtar))
# get_data("https://www.cbe.ncsu.edu/directory/faculty/")





#-*-coding:utf-8-*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sshtunnel import SSHTunnelForwarder
from utils.connection import *
import re
import time
import json
from sqlalchemy import Column, Integer, String

def sshtunnel():
    with SSHTunnelForwarder(
            ('39.104.50.183', 22),
            ssh_username="sc",
            ssh_pkey="./id_rsa",
            remote_bind_address=('127.0.0.1', 5432)
    ) as server:
        server.start()
        print(server.local_bind_port)
        engine = create_engine('postgresql+psycopg2://wyn:weiaizq1314@127.0.0.1:{}/sc_2018'.format(server.local_bind_port))
    return engine

Base = declarative_base()
class User(Base):
    __tablename__ = 'paper1'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    keywords = Column(String)
    author = Column(String)
    issue = Column(String)
    pdf = Column(String)
    time = Column(String)
    findtime = Column(String)

    def __repr__(self):
        return "<User(title='%s', keywords='%s', author='%s', issue='%s', pdf='%s', time='%s', findtime='%s')>" % (
                 self.title, self.keywords, self.author, self.issue, self.pdf, self.time, self.findtime)

metadata = MetaData()

user = Table('paper1', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String(255)),
            Column('keywords', String(255)),
            Column('author', String(255)),
            Column('issue', String(225)),
            Column('pdf', String(255)),
            Column('time', String(20)),
            Column('findtime', String(30))
        )
Base.metadata.create_all(sshtunnel())

class User(object):
    def __init__(self, title, keywords, author, issue, pdf, time, findtime):
        self.title = title
        self.keywords = keywords
        self.author = author
        self.issue = issue
        self.pdf = pdf
        self.time = time
        self.findtime = findtime

mapper(User, user)


# print("Database session created")
Session = sessionmaker(bind=sshtunnel())
session = Session()

infodic={'title':'abc','keywords':'key','author':'sunlei','issue':'fuck','pdf':'www.baidu.com','time':'200000'}
def sqlinput(infodic):
    Session = sessionmaker(bind=sshtunnel())
    session = Session()
    print("Database session created")
    add_user = User(
        title=infodic['title'],
        keywords=infodic['keywords'],
        author=infodic['author'],
        issue=infodic['issue'],
        pdf=infodic['pdf'],
        time=infodic['time'],
        findtime=time.strftime('%Y:%m:%d:%M:%S', time.localtime(time.time()))
    )
    # sql ='''INSERT INTO paper(title,keywords,author,issue,pdf,"time",findtime) VALUES (%s,%s,%s,%s,%s,%s,%s)''',(infodic['title'],infodic['keywords'],infodic['author'],infodic['issue'],infodic['pdf'],infodic['time'],time.strftime('%Y:%m:%d:%M:%S', time.localtime(time.time())))
    # session.execute(sql)
    session.add(add_user)
    session.commit()
# sqlinput(infodic)

# def getArticleInfo(i):#获取所有文章的信息
#     infoList =[]
#     new = {}
#     url = "https://www.sciencedirect.com" + i
#     try:
#         keywords = ""
#         author = ""
#         pdfurl = ""
#         html = fetch(url)
#         title = extract("//span[@class='title-text']/text()", html, False)
#         if title is None or title == "":
#             title = "NO Found"
#         keyword = extract("//div[@class='keyword']/span/text()", html, True)
#         if keyword is None:
#             keywords = "No Found"
#         for key in keyword:
#             keywords = keywords + key + ";"
#         if keywords == "":
#             keywords = "No Found"
#         author_group = extract("//a[@class='author size-m workspace-trigger']", html, True)
#         if author_group is None:
#             author = "No Found"
#         for auth in author_group:
#             firstname = extract("//span[@class='text given-name']/text()", str(etree.tostring(auth)), False)
#             lastname = extract("//span[@class='text surname']/text()", str(etree.tostring(auth)), False)
#             name = str(firstname) + " " + str(lastname)
#             author = author + name + ";"
#         if author == "":
#             author = "No Found"
#         a = extract("//a[@class='anchor PdfDownloadButton']/@href", html, False)
#         if a is None:
#             b = re.findall(r'"linkToPdf":"(.*?)"},"',html)[0]
#             pdfurl = "https://www.sciencedirect.com" + b
#         else:
#             pdfurl = "https://www.sciencedirect.com" + a
#         if pdfurl == "https://www.sciencedirect.com":
#             pdfurl = "No Found"
#         time = extract("//span[@class='size-m']/text()[2]", html, False)
#         if time == "" or time is None:
#             time = "No Found"
#         issue = extract("//a[@class='publication-title-link']/text()", html, False)
#         if issue == "" or issue is None:
#             issue = "No Found"
#         new.update({"title": title, "keywords": keywords, "author": author, "issue": issue, "pdf": pdfurl, "time": time})
#     except Exception as e:
#         print(e)
#         print(url)
#         with open("./TODO.txt","a") as f:
#             f.write(url + "\n")
#             f.close()
#     try:
#         # print(tuple(new.values()))
#         sqlinput(new)
#         infoList.append(new)
#     except Exception as e:
#         print(e)
#         pass
#     return infoList
#
#
#
# with open('./url.txt') as f:
#     line = f.readline()
#     while line:
#         getArticleInfo(line)
#         line = f.readline()
#
