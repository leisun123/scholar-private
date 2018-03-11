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
    html = fetch(url)
    json_content = extract('//script[@type="application/json"]/text()',html,False)
    json_dict = json.loads(json_content)
    # print(json_dict)
    try:
        title = ""
        keywords = ""
        author = ""
        pdfurl = ""
        time = ""
        issue = ""
        abstract =""
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
        a = json_dict.get('authors').get('content')[0].get('$$')
        authordic = {}
        authorlist= []
        affiliation = re.findall(r"'textfn', '_': '(.*?)'",str(a))
        if affiliation:
            affiliation = affiliation[0]
        else:
            affiliation = None
        for i in a:
            name  = ""
            if i.get('#name') == 'author':
                firstname = re.findall(r" 'given-name', '_': '(.*?)'",str(i))
                if firstname:
                    name = firstname[0] + " " + re.findall(r"surname', '_': '(.*?)'",str(i))[0]
                email = re.findall(r"'e-address', '_': '(.*?)'",str(i))
                if email:
                    email = email[0]
                else:
                    email = None
                authordic.update({
                    "name":name,
                    "email":email,
                    "affiliation":affiliation
                                  })
                authorlist.append(authordic)
            print(url)
            print(authorlist)
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
            abs = extract("//p[@id='spar0005']/text()", html, False)
            if abs:
                abstract = abs
            else:
                abstract = "No Found"
            dio = extract("//a[@class='dio']/@href", html, False)
            references = extract("//dd[@class='reference']/span/text()", html, True)
            reference = {}
            if references:
                n = 1
                for each in references:
                    reference[str(n)] = each
            new.update({
                "article_title": title,
                "keywords": keywords,
                "author": str(authorlist),
                "journal_title": issue,
                "pdf": pdfurl,
                "time": time,
                "affiliation":affiliation,
                "abstract":abstract,
                "dio":dio,
                "reference":str(reference)
            })
    except Exception as e:
        print(e)
        print(url)
        with open("./TODO.txt","a") as f:
            f.write(i)
            f.close()
    # try:
    #     # sqlinput(new)
    #     # print(new)
    # except Exception as e:
    #     print(e)
    #     traceback.print_exc()
    #     with open("./TODO.txt","a") as f:
    #         f.write(i)
    #         f.close()
    #     pass
    # return ""


def sqlinput(infodic):
    with SSHTunnelForwarder(
    ('39.104.50.183',22),
    ssh_username = "sc",
    ssh_pkey="./id_rsa",
    remote_bind_address=('127.0.0.1',5432)
    ) as server:
        server.start()
        # print("successfully connected")
        engine = create_engine('postgresql://wyn:weiaizq1314@127.0.0.1:{}/sc_2018'.format(server.local_bind_port))
        Session = sessionmaker(bind=engine)
        session = Session()
        # print("Database session created")
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
    start = 0
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            start = start + 1
            data = q.get()
            getArticleInfo(data)
            queueLock.release()
            if start == 2:
                time.sleep(30)
                return process_data(name,q)
        else:
            queueLock.release()
        time.sleep(random.uniform(2,4))


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