from utils.connection import *
import requests
import json
from selenium import webdriver
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


# dele()
def getArticleInfo(i):#获取所有文章的信息
    new = {}
    url = "https://www.sciencedirect.com" + i
    html = fetch(url)
    print(url)
    try:
        title = ""
        keywords = ""
        author = ""
        pdfurl = ""
        time = ""
        issue = ""
        abstract = ""
        page = ""
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
        authorlist = []
        browser = webdriver.Chrome()
        browser.get(url)
        print("succeed")
        lis = browser.find_elements_by_xpath('//span[@class="content"]')
        for es in lis:
            authordic = {}
            es.click()
            name = ""
            email = ""
            aff = ""
            try:
                name = browser.find_element_by_xpath(
                    "//div[@class='WorkspaceAuthor']/div/span[@class='text given-name']").text + " " + browser.find_element_by_xpath(
                    "//div[@class='WorkspaceAuthor']/div/span[@class='text surname']").text
            except:
                name = None
            try:
                email = browser.find_element_by_xpath("//div[@class='WorkspaceAuthor']/div[@class='e-address']").text
            except:
                email = None
            try:
                aff = browser.find_element_by_xpath("//div[@class='WorkspaceAuthor']/div[@class='affiliation']").text
            except:
                aff = None
            authordic.update({"name": name, "email": email, "affiliation": aff})
            authorlist.append(authordic)
        print(str(authorlist))
        browser.quit()
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
        page = extract("//span[@class='size-m']/a/span/text()", html, False) + extract("//span[@class='size-m']/text()[1]", html, False) + extract("//span[@class='size-m']/text()[2]", html, False) + extract("//span[@class='size-m']/text()[3]", html, False)
        if page is None:
            page = "No Found"
        if issue == "None":
            issue = "No Found"
        abs = extract("//p[@id='spar0005']/text()", html, False)
        if abs:
            abstract = abs
        else:
            abstract = "No Found"
        doi = extract("//a[@class='doi']/@href", html, False)
        references = extract("//dd[@class='reference']/span/text()", html, True)
        reference = {}
        if references:
            n = 1
            for each in references:
                reference[str(n)] = each
        new.update({
            "article_title": str(title),
            "keywords": str(keywords),
            "author": authorlist,
            "journal_title": issue,
            "pdf": str(pdfurl),
            "time": time,
            "abstract":abstract,
            "doi":str(doi),
            "reference":str(reference),
            "page":str(page)
        })
    except Exception as e:
        print(e)
        print(url)
        with open("./TODO.txt","a") as f:
            f.write(str(i))
            f.close()
    try:
        sqlinput(new)
        print(new)
    except Exception as e:
        with open("./TODO.txt","a") as f:
            f.write(str(i))
            f.close()
        print(e)
        traceback.print_exc()
        pass
    return ""
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

# dic = {'doi': 'https://doi.org/10.1016/j.aasri.2014.09.022', 'page': 'Volume 9, 2014, Pages 138-145', 'time': '2014', 'abstract': 'In the progression from CMOS technology to nanotechnology, being able to assess reliability of nano-based electronic circuits is fast becoming necessary. Due to this phenomenon, several computational-based approaches have been proposed for the reliability assessment of nanotechnology-based circuit systems. In quantifying reliability measure of the desired circuit system, faulty gates are considered as the most active part of the system. To have reliable circuit system, apart from its faulty gates, the size of error, ', 'journal_title': 'AASRI Procedia', 'pdf': 'https://www.sciencedirect.com/science/article/pii/S221267161400122X/pdf?md5=a4218894b63c8d2582d18faa8a41bf7b&pid=1-s2.0-S221267161400122X-main.pdf', 'author': "[{'name': 'N.S.S. Singh', 'email': 'narinderjit@petronas.com.my', 'affiliation': 'Fundamental and Applied Sciences Department, Universiti Teknologi PETRONAS, Bandar Seri Iskandar, Tronoh, Perak, Malaysia'}, {'name': 'N.H. Hamid', 'email': None, 'affiliation': 'Electrical and Electronic Engineering Department Universiti Teknologi PETRONAS, Bandar Seri Iskandar, Tronoh, Perak, Malaysia'}, {'name': 'V.S. Asirvadam', 'email': None, 'affiliation': 'Electrical and Electronic Engineering Department Universiti Teknologi PETRONAS, Bandar Seri Iskandar, Tronoh, Perak, Malaysia'}]", 'reference': '{}', 'article_title': 'Error Threshold for Individual Faulty Gates Using Probabilistic Transfer Matrix (PTM)', 'keywords': 'Reliability;Reliability Assessment;Individual Faulty Gates;Exact Error Threshold;Probabilistic Transfer Matrix (PTM);'}
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
        attit = str(infodic['article_title'])
        keyw = str(infodic['keywords'])
        aut = (infodic['author'])
        print(type(aut))
        joutit = str(infodic['journal_title'])
        tim = str(infodic['time'])
        pd = str(infodic['pdf'])
        abs = str(infodic['abstract'])
        do = str(infodic['doi'])
        pag = str(infodic['page'])
        ref = str(infodic['reference'])
        sql = '''INSERT INTO paper("journal title",keywords,abstract,doi,"article title",pdf,"time",findtime,page,"references") VALUES {}'''.format((joutit,keyw,abs,do,attit,pd,tim,time.strftime('%Y-%m-%d', time.localtime(time.time())),pag,ref))
        session.execute(sql)
        session.commit()
        server.stop()

# sqlinput(dic)
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
