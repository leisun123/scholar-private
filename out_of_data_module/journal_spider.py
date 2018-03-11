#-*-coding:utf-8-*-

from utils.connection import *
import requests
import json
# from threadpool import *
import time
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
import re
# from ScholarConfig.config import proxies
from ScholarConfig.config import USER_AGENT
import threading
import os


if os.path.exists('./url.txt'):
    os.remove('./url.txt')


# def getJournalList(s): #获取所有的title名字与链接
#     journalURL = "https://www.sciencedirect.com/science/journals/" + s + "/full-text-access"
#     infoDic = {}
#     try:
#         html = fetch(journalURL)
#     except:
#         return getJournalList(s)
#     info_1 = {}
#     info_2 = {}
#     try:
#         tmp = extract('//li[@class="browseList browseColFirst"]',html,multi=True)
#         for i in tmp:
#             url = extract('//a/@href', html_source=str(etree.tostring(i)))
#             res = fetch("https://www.sciencedirect.com" + url)
#             title = extract('//link[@rel="canonical"]/@href', res, False)
#             title = title.split('al/')[-1]
#             info_1[url] = title
#             time.sleep(random.uniform(3,6))
#     except:
#         pass
#     print(info_1)
#     time.sleep(random.uniform(60,120))
#     getIssueURL(info_1)
#     time.sleep(random.uniform(60,120))
#     for i in range(1,11):
#         urls = "https://www.sciencedirect.com/science/browsescroll/journals/" + s + "/full-text-access/begidx" + str(i*50) + "/rwpos/0"
#         try:
#             headers = {
#                 "User-Agent":USER_AGENT
#             }
#             r = requests.Session().get(urls,headers=headers)
#             time.sleep(random.uniform(5,10))
#             json_response = r.content.decode()
#             json_dict = json.loads(json_response)
#             if json_dict:
#                 # print(json_dict)
#                 for each in json_dict:
#                     for key in each.keys():
#                         if key == "I":
#                             url = "/science/journal/" + each[key]
#                             res = fetch("https://www.sciencedirect.com" + url)
#                             title = extract('//link[@rel="canonical"]/@href', res, False)
#                             title = title.split('al/')[-1]
#                             info_2[url] = title
#                         else:
#                             pass
#                 time.sleep(random.uniform(120,240))
#                 getIssueURL(info_2)
#             else:
#                 break
#         except Exception as e:
#             print(e)
#             print(urls)
#             pass
#     return ""
infoDic = {
    "/science/journal/22126716":"aasri-procedia",
    "/science/journal/18762859":"academic-pediatrics"
}
def getIssueURL(infoDic): #获取所有article的链接
    urlList = []
    for i in infoDic.keys():
        a = infoDic[i]
        for y in range(2000,2019):
            s = i.split('e')[-1] + "/year/" + str(y) + "/issues"
            url = "https://www.sciencedirect.com" + s
            print(url)
            try:
                headers = {
                    "User-Agent": USER_AGENT
                }
                r = requests.get(url,headers=headers)
                time.sleep(random.uniform(5, 10))
                json_response = r.content.decode()
                dict_json = json.loads(json_response)
                if dict_json.__contains__("data"):
                    dic = dict_json["data"][0]
                    urlinfo = "https://www.sciencedirect.com/journal/" + a + dic["uriLookup"]
                    res = fetch(urlinfo)
                    st = extract("//a[@class='anchor article-content-title u-margin-top-xs u-margin-bottom-s']/@href",res,True)
                    with open('./url.txt', 'a') as f:
                        for u in st:
                            f.write(u + '\n')
                        f.close()
                        print("open successfully")
                else:
                    continue
            except Exception as e:
                print(e)
        time.sleep(random.uniform(6,12))
    return urlList


start_time = time.time()
# s = "a"
# getJournalList(s)
# info = {'/science/journal/22140085': 'biochimie-open', '/science/journal/0304419X': 'biochimica-et-biophysica-acta-bba-reviews-on-cancer', '/science/journal/03044157': 'biochimica-et-biophysica-acta-bba-reviews-on-biomembranes', '/science/journal/13881981': 'biochimica-et-biophysica-acta-bba-molecular-and-cell-biology-of-lipids', '/science/journal/03766357': 'behavioural-processes', '/science/journal/15216918': 'best-practice-and-research-clinical-gastroenterology', '/science/journal/03024598': 'bioelectrochemistry-and-bioenergetics', '/science/journal/15216942': 'best-practice-and-research-clinical-rheumatology', '/science/journal/01664328': 'behavioural-brain-research', '/science/journal/03009084': 'biochimie', '/science/journal/09503528': 'baillieres-clinical-gastroenterology', '/science/journal/0006291X': 'biochemical-and-biophysical-research-communications', '/science/journal/00063207': 'biological-conservation', '/science/journal/09503501': 'baillieres-clinical-anaesthesiology', '/science/journal/1369703X': 'biochemical-engineering-journal', '/science/journal/22105336': 'basal-ganglia', '/science/journal/18749399': 'biochimica-et-biophysica-acta-bba-gene-regulatory-mechanisms', '/science/journal/00052728': 'biochimica-et-biophysica-acta-bba-bioenergetics', '/science/journal/18788181': 'biocatalysis-and-agricultural-biotechnology', '/science/journal/09254439': 'biochimica-et-biophysica-acta-bba-molecular-basis-of-disease', '/science/journal/23148535': 'beni-suef-university-journal-of-basic-and-applied-sciences', '/science/journal/22126198': 'bioactive-carbohydrates-and-dietary-fibre', '/science/journal/15216896': 'best-practice-and-research-clinical-anaesthesiology', '/science/journal/03044165': 'biochimica-et-biophysica-acta-bba-general-subjects', '/science/journal/00153796': 'biochemie-und-physiologie-der-pflanzen', '/science/journal/03051978': 'biochemical-systematics-and-ecology', '/science/journal/01674781': 'biochimica-et-biophysica-acta-bba-gene-structure-and-expression', '/science/journal/01674838': 'biochimica-et-biophysica-acta-bba-protein-structure-and-molecular-enzymology', '/science/journal/02085216': 'biocybernetics-and-biomedical-engineering', '/science/journal/2452199X': 'bioactive-materials', '/science/journal/00057967': 'behaviour-research-and-therapy', '/science/journal/15675394': 'bioelectrochemistry', '/science/journal/00052760': 'biochimica-et-biophysica-acta-bba-lipids-and-lipid-metabolism', '/science/journal/10773150': 'biochemical-and-molecular-medicine', '/science/journal/22146474': 'bba-clinical', '/science/journal/15216926': 'best-practice-and-research-clinical-haematology', '/science/journal/1521690X': 'best-practice-and-research-clinical-endocrinology-and-metabolism', '/science/journal/00057894': 'behavior-therapy', '/science/journal/15709639': 'biochimica-et-biophysica-acta-bba-proteins-and-proteomics', '/science/journal/09503536': 'baillieres-clinical-haematology', '/science/journal/09503552': 'baillieres-clinical-obstetrics-and-gynaecology', '/science/journal/00062952': 'biochemical-pharmacology', '/science/journal/14391791': 'basic-and-applied-ecology', '/science/journal/22145796': 'big-data-research', '/science/journal/24055808': 'biochemistry-and-biophysics-reports'}
# getIssueURL(info)
getIssueURL(infoDic)
print(time.time()-start_time)


