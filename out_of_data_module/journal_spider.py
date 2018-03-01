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

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

def getJournalList(journalURL): #获取所有的title名字与链接
    infoDic = {}
    html = fetch(journalURL)
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
    except:
        pass
    for i in range(1,11):
        urls = "https://www.sciencedirect.com/science/browsescroll/journals/a/full-text-access/begidx" + str(i*50) + "/rwpos/0"
        try:
            user_agent = random.choice(USER_AGENTS)
            headers = {
                "User-Agent":user_agent
            }
            r = requests.get(urls,headers=headers)
            json_response = r.content.decode()
            json_dict = json.loads(json_response)
            if json_dict:
                # print(json_dict)
                for each in json_dict:
                    for key in each.keys():
                        if key == "I":
                            url = each[key]
                            res = fetch("https://www.sciencedirect.com/science/journal/" + url)
                            # print(url)
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
        infoDic = dict(info_1,**info_2)
    # print(info_2)
    # print(info_1)
    return infoDic

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
                r = requests.get(url)
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
        if title is None or title == "":
            title = "NO Found"
        keyword = extract("//div[@class='keyword']/span/text()", html, True)
        if keyword is None:
            keywords = "No Found"
        for key in keyword:
            keywords = keywords + key + ";"
        if keywords == "":
            keywords = "No Found"
        author_group = extract("//a[@class='author size-m workspace-trigger']", html, True)
        if author_group is None:
            author = "No Found"
        for auth in author_group:
            firstname = extract("//span[@class='text given-name']/text()", str(etree.tostring(auth)), False)
            lastname = extract("//span[@class='text surname']/text()", str(etree.tostring(auth)), False)
            name = str(firstname) + " " + str(lastname)
            author = author + name + ";"
        if author == "":
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
    # try:
    #     jsObj = json.dumps(new)
    #     with open("F:/study/python/res.json","a") as f:
    #         f.write(jsObj)
    #         f.close()
    # except:
    #     pass
    # print(new)
    try:
        sqlinput(new)
    except Exception as e:
        print(e)
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
        sql = '''INSERT INTO paper(title,keywords,author,issue,pdf,"time",findtime) VALUES {}'''.format((tit,keyw,aut,iss,pd,tim,time.strftime('%Y:%m:%d:%M:%S', time.localtime(time.time()))))
        session.execute(sql)
        session.commit()
        server.stop()




journal_list_url = "https://www.sciencedirect.com/science/journals/a/full-text-access"
slist = {}
urlList = []
infoDic = []
slist = getJournalList(journal_list_url)
urlList = getIssueURL(slist)

print(len(urlList))
start_time = time.time()
pool = ThreadPool(3)
res = makeRequests(getArticleInfo,urlList)
[pool.putRequest(req) for req in res]
time.sleep(2)
pool.wait()
print(time.time()-start_time)