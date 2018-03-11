#coding:utf-8

import json
from utils.connection import *
import re
import traceback
def get(url):
    html = fetch(url)
    json_content = extract('//script[@type="application/json"]/text()',html,False)
    json_dict = json.loads(json_content)
    # print(json_content)
    a = json_dict.get('authors').get('content')[0].get('$$')
    authordic = {}
    authorlist= []
    affiliation = re.findall(r"'textfn', '_': '(.*?)'",str(a),re.S)
    if not affiliation:
        traceback.print_exc()
    # affiliation = affiliation[0]
    for i in a:
        name  = ""
        if i.get('#name') == "author":
            firstname = re.findall(r" 'given-name', '_': '(.*?)'",str(i),re.S)
            if firstname:
                name = firstname[0] + " " + re.findall(r"surname', '_': '(.*?)'",str(i),re.S)[0]
            email = re.findall(r"'e-address', '_': '(.*?)'",str(i),re.S)
            if not email:
                email = None
            else:
                email = email[0]
            authordic.update({
                "name":name,
                "email":email,
                "affiliation":affiliation
                              })
            print(authordic)
            authorlist =
            print(authorlist)
            print("\n\n")

    print(authorlist)
    print("----------------------------------------------------------\n")
# print(json_dict)

get("https://www.sciencedirect.com/science/article/pii/S2212671614000109")
get("https://www.sciencedirect.com/science/article/pii/S2212671614000134")