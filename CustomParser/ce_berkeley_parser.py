#coding:utf-8
"""
@file:      ce_berkeley_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/26 20:18
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from BaseModule.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass
from utils.connection import extract
from ScholarConfig.ce_berkeley_rule  import RULES,BASE_URL
from nameparser import HumanName
PS_ERROR = lambda func:except_pass(func,ModelName = 'ce_berkeley')

class CEBerkeleyClass(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(CEBerkeleyClass, self).__init__()
        self.generate_all_method()

    
    def _generate_avatar(self):
        self.avatar = '{}{}'.format(BASE_URL,extract(RULES["avatar"],self.sec))
    def _generate_firstName(self):
        tmp = extract(RULES["name"],self.sec)
        self.firstName = HumanName(tmp).first
    def _generate_lastName(self):
        tmp = extract(RULES["name"],self.sec)
        self.lastName = HumanName(tmp).last
    def _generate_organization(self):
        self.organization = "University of California at Berkeley"
    def _generate_major(self):
        self.major = "Civil and Environmental Engineering"
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
        tmp = extract(RULES["phone"],self.sec)
        if tmp is not None:
            self.phone = tmp.strip()
    def _generate_email(self):
        self.email = extract(RULES["email"],self.sec).strip()
    def _generate_website(self):
        pass
    def _generate_cooperation(self):
        self.cooperation.append(extract(RULES["cooperation"],self.sec))
    def _generate_bio(self):
        self.bio = extract(RULES["bio"],self.sec)
    
    def _generate_keywords(self):
        self.keywords.append(extract(RULES["keywords"],self.sec))
        
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
    html= fetch("http://www.me.berkeley.edu/people/faculty/m-reza-alam")
#    print(html)
    a=extract(RULES["phone"],html)
    print(a)