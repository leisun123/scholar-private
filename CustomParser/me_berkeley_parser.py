#coding:utf-8
"""
@file:      me_berkeley_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 19:09
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from BaseModule.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from utils.connection import extract
from ScholarConfig.me_berkeley_rule  import RULES
from nameparser import HumanName
PS_ERROR = lambda func:except_pass(func,ModelName = 'me_berkeley')

class MEBerkeleyClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(MEBerkeleyClass, self).__init__()
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
        self.organization = "University of California at Berkeley"
    def _generate_major(self):
        self.major = "Mechanical Engineering"
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
        pass
        
    def _generate_email(self):
        a = str(self.sec).replace('arrow@2x.png','')
        emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
        import re
        tmp = re.search(emailRegex,a)
        if tmp is not None:
            self.email=tmp.group()

    def _generate_website(self):
        pass
    
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
    html= fetch("http://www.me.berkeley.edu/people/faculty")
    #print(html)
    a=extract(RULES["item_url"],html,multi=True)
    print(a)