#coding:utf-8
"""
@file:      caee_utexas_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 4:56
@description:
            --
"""
from lxml import etree

from BaseClass.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from db.SqlHelper import SqlHelper
from utils.connection import extract
from ScholarConfig.caee_utexas_rule import RULES
from nameparser import HumanName

PS_ERROR = lambda func:except_pass(func,ModelName = 'caee_utexas')

class CaeeUtexasClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(CaeeUtexasClass, self).__init__()
        self.generate_all_method()
        parm=self.set_value()
        sqlhelper=SqlHelper()
        sqlhelper.insert_scholar_thesis(**parm)
    
    def _generate_avatar(self):
        self.avatar = extract(RULES["avatar"],self.sec)
    def _generate_firstName(self):
        tmp = extract(RULES["name"],self.sec)
        self.firstName = HumanName(tmp).first
    def _generate_lastName(self):
        tmp = extract(RULES["name"],self.sec)
        self.lastName = HumanName(tmp).last
    def _generate_organization(self):
        self.organization = "The University of Texas at Austin"
    def _generate_major(self):
        self.major = "Civil,Architectural and Environmental Engineering"
    def _generate_title(self):
        title_1=extract(RULES["title_1"],self.sec)
        title_2=extract(RULES["title_2"],self.sec)
        title_3=extract(RULES["title_3"],self.sec)
        if title_1 is None:
            title_1 = ""
        if title_2 is None:
            title_2 = ""
        if title_3 is None:
            title_3 = ""
        self.title = "{}{}{}".format(title_1,title_2,title_3)
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
        a=extract(RULES["info"],self.sec,multi=True)[-1]
        b=a.xpath('string(.)')
        if "Phone" in b:
            c=b.replace('Email','').replace('Phone','')\
                .replace('Office','').strip().split(":")
            self.phone = c[2]
        else:
            self.phone = None
            
    def _generate_email(self):
        a=extract(RULES["info"],self.sec,multi=True)[-1]
        b=a.xpath('string(.)')
        if "Email" in b:
            c=b.replace('Email','').replace('Phone','')\
                .replace('Office','').strip().split(":")
            self.email = c[1]
        else:
            self.email = None
    def _generate_website(self):
        if "My Website" in self.sec:
            self.website = extract(RULES["website"],self.sec)
        else:
            self.website = None
    def _generate_cooperation(self):
            tmp = extract(RULES["cooperation"],self.sec)
            if tmp is not None:
                if ";" in tmp:
                    self.cooperation = tmp.split(";")
                else:
                    self.cooperation.append(tmp)
            else:
                self.cooperation = []
        
    def _generate_bio(self):
        pass
    def _generate_keywords(self):
        tmp = extract(RULES["keywords"],self.sec)
        if tmp is not None:
            if "," in tmp:
                self.keywords = tmp.split(",")
            else:
                self.keywords.append(tmp)
        else:
            self.keywords = []
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
    html= fetch("http://www.caee.utexas.edu/faculty/directory/wright")
    sec = extract(RULES["item_url"],html,multi=True)
    html_1=fetch("http://www.caee.utexas.edu/faculty/directory/gloyna")
    a=extract(RULES["info"],html_1,multi=True)[-1]
    b=extract(RULES["cooperation"],html)
    c=[]
    print(html)