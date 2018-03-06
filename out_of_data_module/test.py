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
from ScholarConfig.config import USER_AGENT
import threading
import queue
import traceback
from out_of_data_module.repaire import dele
exitFlag = 0


dele()
def getArticleInfo(i):#获取所有文章的信息
    new = {}
    url = "https://www.sciencedirect.com" + i
    try:
        title = ""
        keywords = ""
        author = ""
        pdfurl = ""
        time = ""
        issue = ""
        html = fetch(url)
        title = extract("//span[@class='title-text']/text()", html, False)
        if str(title) == "None":
            title = "NO Found"
        keyword = extract("//div[@class='keyword']/span/text()", html, True)
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
            b = re.findall(r'"linkToPdf":"(.*?)","',html)[0]
            if '"},"isCorpReq"' in b:
                b = b.split('"},"isCorpReq"')[0]
            pdfurl = "https://www.sciencedirect.com" + b
        else:
            pdfurl = "https://www.sciencedirect.com" + a
        if pdfurl == "https://www.sciencedirect.com":
            pdfurl = "No Found"
        time = extract("//span[@class='size-m']/text()[2]", html, False)
        if str(time) == "None":
            time = "No Found"
        issue = extract("//a[@class='publication-title-link']/text()", html, False)
        if issue == "None":
            issue = "No Found"
        new.update({"title": title, "keywords": keywords, "author": author, "issue": issue, "pdf": pdfurl, "time": time})
    except Exception as e:
        print(e)
        print(url)
        with open("./TODO.txt","a") as f:
            f.write(url + "\n")
            f.close()
    try:
        sqlinput(new)
        print(new)
    except Exception as e:
        print(e)
        traceback.print_exc()
        pass
    return ""

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
        sql = '''INSERT INTO paper(title,issue,keywords,pdf,"time",findtime,author) VALUES {}'''.format((tit,iss,keyw,pd,tim,time.strftime('%Y-%m-%d', time.localtime(time.time())),aut))
        session.execute(sql)
        session.commit()
        server.stop()


task = []
with open('./new_url.txt') as f:
    line = f.readline()
    while line:
        task.append(line)
        line = f.readline()

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        process_data(self.name,self.q)

def process_data(name,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            getArticleInfo(data)
            print(name + "正在运行")
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(2)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
queueLock = threading.Lock()
workQueue = queue.Queue(len(task))
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for i in task:
    workQueue.put(i)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()