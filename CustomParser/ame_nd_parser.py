#coding:utf-8
"""
@file:      common_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/1 1:34
@description:
            --
"""
from BaseClass.ThesisClass import ThesisInfo
from SampleData.ame_nd import organization,major
from nameparser import HumanName
import re

class AmeNdClass(ThesisInfo):
    def __init__(self, sec=None, parse_data=None):
        """
        :param sec: item url
        """
        self.sec = sec
        self.parse_data = parse_data
        super(AmeNdClass, self).__init__()
        self.generate_all_method()

    
    def _generate_avatar(self):
        if "avatar" in self.parse_data.keys():
            if self.parse_data["avatar"]:
                regex = '[a-zA-z]+://[^\s]*'
                res = re.search(regex, str(self.parse_data["avatar"]))
                self.avatar = res.group()
    def _generate_firstName(self):
        if "name" in self.parse_data.keys():
            if self.parse_data["name"]:
                self.firstName = HumanName(self.parse_data["name"]).first
    def _generate_lastName(self):
        if "name" in self.parse_data.keys():
            if self.parse_data["name"]:
                self.lastName = HumanName(self.parse_data["name"]).last
    def _generate_organization(self):
        self.organization = organization
    def _generate_major(self):
        self.major = major
    def _generate_title(self):
        if "title" in self.parse_data.keys():
            if self.parse_data["title"]:
                self.title = self.parse_data["title"]
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
        if "phone" in self.parse_data.keys():
            if self.parse_data["phone"]:
               self.phone = self.parse_data["phone"]
    def _generate_email(self):
        if "email" in self.parse_data.keys():
            if self.parse_data["email"]:
                self.email = self.parse_data["email"]
    def _generate_website(self):
        if "website" in self.parse_data.keys():
            if self.parse_data["website"]:
                regex = '"(.*?)"'
                res = re.search(regex, str(self.parse_data["website"]))
                self.website = res.group()
    def _generate_cooperation(self):
        if "cooperation" in self.parse_data.keys():
            if self.parse_data["cooperation"]:
                self.cooperation.append(self.parse_data["cooperation"])
    def _generate_bio(self):
        if "bio" in self.parse_data.keys():
            if self.parse_data["bio"]:
                self.bio = self.parse_data["bio"]
    def _generate_keywords(self):
        if "keywords" in self.parse_data.keys():
            if self.parse_data["keywords"]:
                self.keywords.append(self.parse_data["keywords"])
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
