#coding:utf-8
"""
@file:      tmi_utexas_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 12:06
@description:
            --
"""
from lxml import etree

from BaseClass.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from db.SqlHelper import SqlHelper
from utils.connection import extract
from ScholarConfig.tmi_utexas_rule import RULES
from nameparser import HumanName
from TaskFeed.tmi_utexas_task import TmiUtexasTask
PS_ERROR = lambda func:except_pass(func,ModelName = 'caee_utexas')

class TmiUtexasClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(TmiUtexasClass, self).__init__()
        self.generate_all_method()
        parm=self.set_value()
        sqlhelper=SqlHelper(TmiUtexasTask.logger)
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
        self.major = "Materials Science & Engineering"
    def _generate_title(self):
        self.title = extract(RULES["title"],self.sec)
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
        self.phone = extract(RULES["phone"],self.sec)
            
    def _generate_email(self):
        self.email = extract(RULES["email"],self.sec)
    def _generate_website(self):
        self.website = extract(RULES["website"],self.sec)
    def _generate_cooperation(self):
        if "Research Interest" in self.sec:
            self.cooperation = extract(RULES["cooperation"],self.sec,multi=True)
        
    def _generate_bio(self):
        pass
    def _generate_keywords(self):
        a = extract(RULES["keywords"],self.sec)
        if  a is not None:
            self.keywords.append(a)
  
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
    html= fetch("http://tmi.utexas.edu/people/type/faculty/")
    a=extract(RULES["item_url"],html,multi=True)
    print(a)