#-*-coding:utf-8-*-

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
from ScholarConfig import proxies
from ScholarConfig.config import USER_AGENT




pool = ThreadPool(3)

def getJournalList(s): #获取所有的title名字与链接
    journalURL = "https://www.sciencedirect.com/science/journals/" + s + "/full-text-access"
    infoDic = {}
    try:
        html = fetch(journalURL)
    except:
        return getJournalList(s)
    info_1 = {}
    info_2 = {}
    try:
        tmp = extract('//li[@class="browseList browseColFirst"]',html,multi=True)
        for i in tmp:
            url = extract('//a/@href', html_source=str(etree.tostring(i)))
            res = fetch("https://www.sciencedirect.com" + url)
            title = extract('//link[@rel="canonical"]/@href', res, False)
            title = title.split('al/')[-1]
            info_1[url] = title
            time.sleep(random.uniform(3,5))
    except:
        pass
    time.sleep(random.uniform(30,60))
    urlList1 = getIssueURL(info_1)
    time.sleep(random.uniform(30,60))
    res = makeRequests(getArticleInfo, urlList1)
    [pool.putRequest(req) for req in res]
    pool.wait()
    for i in range(1,11):
        urls = "https://www.sciencedirect.com/science/browsescroll/journals/" + s + "/full-text-access/begidx" + str(i*50) + "/rwpos/0"
        try:
            headers = {
                "User-Agent":USER_AGENT
            }
            r = requests.get(urls,headers=headers,proxies=proxies)
            json_response = r.content.decode()
            json_dict = json.loads(json_response)
            if json_dict:
                # print(json_dict)
                for each in json_dict:
                    for key in each.keys():
                        if key == "I":
                            url = "/science/journal/" + each[key]
                            res = fetch("https://www.sciencedirect.com" + url)
                            title = extract('//link[@rel="canonical"]/@href', res, False)
                            title = title.split('al/')[-1]
                            info_2[url] = title
                        else:
                            pass
            else:
                break
        except Exception as e:
            print(e)
            print(urls)
            pass
        time.sleep(random.uniform(30, 60))
        urlList2 = getIssueURL(info_2)
        time.sleep(random.uniform(30, 60))
        reqs = makeRequests(getArticleInfo, urlList2)
        [pool.putRequest(req) for req in reqs]
        pool.wait()
    return ""

def getIssueURL(infoDic): #获取所有article的链接
    urlList = []
    for i in infoDic.keys():
        a = infoDic[i]
        articleurlDic = []
        for y in range(2000,2019):
            s = i.split('e')[-1] + "/year/" + str(y) + "/issues"
            url = "https://www.sciencedirect.com" + s
            print(url)
            try:
                headers = {
                    "User-Agent": USER_AGENT
                }
                r = requests.get(url,headers=headers,proxies=proxies)
                json_response = r.content.decode()
                dict_json = json.loads(json_response)
                if dict_json.__contains__("data"):
                    dic = dict_json["data"][0]
                    urlinfo = "https://www.sciencedirect.com/journal/" + a + dic["uriLookup"]
                    res = fetch(urlinfo)
                    articleurlDic = extract("//a[@class='anchor article-content-title u-margin-top-xs u-margin-bottom-s']/@href",res,True)
                    urlList = urlList + articleurlDic
                else:
                    continue
            except Exception as e:
                print(e)
            time.sleep(random.uniform(4,10))
        time.sleep(random.uniform(6,12))
    return urlList

def getArticleInfo(i):#获取所有文章的信息
    new = {}
    url = "https://www.sciencedirect.com" + i
    try:
        keywords = ""
        author = ""
        pdfurl = ""
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
        # sqlinput(new)
        print(new)
    except Exception as e:
        print(e)
        pass
    time.sleep(random.uniform(6,10))
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
        sql = '''INSERT INTO paper(title,keywords,author,issue,pdf,"time",findtime) VALUES {}'''.format((tit,keyw,aut,iss,pd,tim,time.strftime('%Y-%m-%d', time.localtime(time.time()))))
        session.execute(sql)
        session.commit()
        server.stop()


start_time = time.time()
s = "a"
# slist = {}
# urlList = []
# infoDic = []
getJournalList(s)
# time.sleep(random.uniform(60,120))
# urlList = getIssueURL(slist)
# time.sleep(random.uniform(60,120))
#
# print(len(urlList))
# pool = ThreadPool(4)
# res = makeRequests(getArticleInfo,urlList)
# [pool.putRequest(req) for req in res]
# pool.wait()
print(time.time()-start_time)