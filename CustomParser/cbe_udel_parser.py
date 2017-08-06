#coding:utf-8
"""
@file:      cbe_udel
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/6 9:51
@description:
            --
"""
from BaseClass.ThesisClass import ThesisInfo
from BaseClass.common_task import CommonTask
from SampleData.cbe_udel import *
from nameparser import HumanName
import re
from utils.connection import extract


class CBEUdelClass(ThesisInfo):
    def __init__(self, sec=None, parse_data=None):
        """
        :param sec: item url
        """
        self.sec = sec
        self.parse_data = parse_data
        super(CBEUdelClass, self).__init__()
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
        if phone_rule:
            tmp = extract(phone_rule, self.sec)
            if tmp:
                self.phone = tmp.xpath('string(.)').strip().replace('Phone:','')
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
        if bio_rule:
            self.bio = extract(bio_rule, self.sec)
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
    from SampleData.cbe_udel import base_url,sample_url,data,item_url_rule
    CBETask = CommonTask(website_name=CBEUdelClass.__name__,
                   custom_parser=CBEUdelClass,
                   base_url=base_url,
                   sample_url=sample_url,
                   data=data,
                   item_url_rule=item_url_rule
                   )
    CBETask.run()
    print(CBETask.count)