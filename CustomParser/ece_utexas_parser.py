#coding:utf-8
"""
@file:      ece_utexas_edu
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 7:39
@description:
            --
"""

from BaseClass.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from utils.connection import extract
from ScholarConfig.ece_utexas_rule  import RULES
from nameparser import HumanName
PS_ERROR = lambda func:except_pass(func,ModelName = 'ece_utexas')

class ECEUtexasClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(ECEUtexasClass, self).__init__()
        self.generate_all_method()

    
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
        self.major = "Electrical and Computer Engineering"
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
       tmp = extract(RULES["email-1"],self.sec)
       if tmp is not None:
           self.email = tmp
       else:
           self.email = extract(RULES["email-2"],self.sec)
    def _generate_website(self):
        if 'Personal Website' in self.sec:
            tmp = extract(RULES["website-1"],self.sec)
            if tmp is not None:
                self.website = tmp
            else:
                self.website = extract(RULES["website-2"],self.sec)
    def _generate_cooperation(self):
        self.cooperation = extract(RULES["cooperation"],self.sec,multi=True)
        
    def _generate_bio(self):
        self.bio = extract(RULES["bio"],self.sec)

    def _generate_keywords(self):
        self.keywords = extract(RULES["keywords"],self.sec,multi=True)
        
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
    html= fetch("http://www.ece.utexas.edu/people/faculty/david-soloveichik")
    #print(html)
    a=extract(RULES["keywords"],html)
    print(a)