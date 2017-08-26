#coding:utf-8
"""
@file:      cs_utexas_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/16 17:49
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

import re
from datetime import datetime

from lxml import etree

from BaseModule.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from db.SqlHelper import SqlHelper
from utils.connection import extract
from ScholarConfig.cs_utexas_rule import RULES
from nameparser import HumanName
from TaskFeed.cs_utexas_task import CSUtexasTask
PS_ERROR = lambda func:except_pass(func,ModelName = 'cs_utexas')

class CSUtexasClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(CSUtexasClass, self).__init__()
        self.generate_all_method()

    
    def _generate_avatar(self):
        self.avatar = extract(RULES["avatar"],self.sec)
    def _generate_firstName(self):
        tmp = extract(RULES["info"],self.sec,multi=True)[0]
        self.firstName = HumanName(extract("//strong/a/text()",str(etree.tostring(tmp)))).first
    def _generate_lastName(self):
        tmp = extract(RULES["info"],self.sec,multi=True)[0]
        self.lastName = HumanName(extract("//strong/a/text()",str(etree.tostring(tmp)))).last
    def _generate_organization(self):
        self.organization = "The University of Texas at Austin"
    def _generate_major(self):
        self.major = "Computer science"
    def _generate_title(self):
        tmp = extract(RULES["info"],self.sec,multi=True)[0]
        if tmp is not None:
            tmp_1 = tmp.xpath('string(.)')
            if tmp_1 is not None:
                self.title = tmp_1.split('\\n')[2].strip()
    def _generate_birth(self):
        pass
    def _generate_country(self):
        pass
    def _generate_state(self):
        pass
    def _generate_maincity(self):
        if len(self.city) != 0:
            self.maincity = self.city[0]
    def _generate_phone(self):
        tmp=extract(RULES["info"],self.sec,multi=True)[1]
        if tmp is not None:
            tmp_1 = tmp.xpath('string(.)')
            if tmp_1 is not None:
                #print(tmp.xpath('string(.)').split('\\n')[1].strip().split(','))
                if len(tmp_1.split('\\n')[1].strip().split(','))==4:
                    self.phone=(tmp_1.split('\\n')[1].strip().split(',')[2])
                elif len(tmp_1.split('\\n')[1].strip().split(','))==3:
                    if '@' not in (tmp.xpath('string(.)').split('\\n')[1].strip().split(',')[1]):
                        self.phone=(tmp_1.split('\\n')[1].strip().split(',')[1])
                else:
                    self.phone=None
    def _generate_email(self):
        tmp=extract(RULES["info"],self.sec,multi=True)[1]
        if tmp is not None:
            tmp_1 = tmp.xpath('string(.)')
            if tmp_1 is not None:
                emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
                a=(tmp.xpath('string(.)').split('\\n')[1].strip())
                import re
                b=re.search(emailRegex,str(a))
                if b is not None:
                    self.email=b.group(0)
                else:
                    self.email=None
    def _generate_website(self):
        tmp = extract(RULES["info"],self.sec,multi=True)[1]
        if tmp is not None:
            tmp_1 = tmp.xpath('string(.)')
            if tmp_1 is not None:
                a=extract("//a/@href",str(etree.tostring(tmp)),multi=True)
                if len(a)==2:
                    self.website=a[1]
                else:
                    self.website=None
    def _generate_cooperation(self):
        pass
    def _generate_bio(self):
        pass
    def _generate_keywords(self):
        self.keywords = extract(RULES["keyword"],self.sec,multi=True)
    def _generate_city(self):
        pass
    def _generate_time(self):
        pass
    def _generate_keywordKeys(self):
        self.keywordKeys = [i for i in range(1,len(self.keywords)+1)]
    def _generate_cityKeys(self):
        self.cityKeys = [i for i in range(1,len(self.city)+1)]
    def _generate_timeKeys(self):
        self.timeKeys = [i for i in range(1,len(self.timeKeys)+1)]

if __name__ == '__main__':
    from utils.connection import fetch
    html=fetch("https://www.cs.utexas.edu/faculty")
    sec = extract(RULES["item"],html,multi=True)
    for i in sec:
        if i is not None:
            # tmp=extract(RULES["info"],str(etree.tostring(i)),multi=True)[1]
            # if tmp is not None:
            #     a=extract("//a/@href",str(etree.tostring(tmp)),multi=True)
            #     if len(a)==2:
            #         print(a[1])
            #     else:
            #         print(None)
            
            tmp=extract(RULES["keyword"],str(etree.tostring(i)),multi=True)
            print(tmp)
        
        
        
    