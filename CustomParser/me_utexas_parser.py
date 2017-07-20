#coding:utf-8
"""
@file:      me.utexas
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/17 1:57
@description:
            --
"""
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
import re
from datetime import datetime

from lxml import etree

from BaseClass.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from db.SqlHelper import SqlHelper
from utils.connection import extract
from ScholarConfig.me_utexas_rule import RULES
from TaskFeed.me_utexas_task import MeUtexasTask
PS_ERROR = lambda func:except_pass(func,ModelName = 'cs_utexas')

class MeUtexasClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(MeUtexasClass, self).__init__()
        self.generate_all_method()
        parm=self.set_value()
        sqlhelper=SqlHelper()
        sqlhelper.insert_scholar_thesis(**parm)
    
    def _generate_avatar(self):
        self.avatar = extract(RULES["avatar"],self.sec)
    def _generate_firstName(self):
        self.firstName = extract(RULES["name"],self.sec).split(',')[0]
    def _generate_lastName(self):
        self.lastName = extract(RULES["name"],self.sec).split(',')[1]
    def _generate_organization(self):
        self.organization = "The University of Texas at Austin"
    def _generate_major(self):
        self.major = "Mechanical Engineering"
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
        tmp=extract(RULES["info"],self.sec,multi=True)[-1]
        if tmp is not None :
            a=tmp.xpath('string(.)')
            if a is not None :
                self.phone = a.split(':')[2]
    def _generate_email(self):
        self.email=extract(RULES["email"],self.sec)

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
        pass
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
    html=fetch("http://me.utexas.edu/faculty/faculty-directory")
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
            #print(etree.tostring(i))
            tmp=extract(RULES["info"],str(etree.tostring(i)),multi=True)[-1]
            if tmp is not None :
                a=tmp.xpath('string(.)')
                if a is not None :
                    print(a.split(':')[2])
        
    