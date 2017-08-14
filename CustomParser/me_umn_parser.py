#coding:utf-8
"""
@file:      me_umn_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-14 下午4:10
@description:
            --
"""

from BaseClass.ThesisClass import ThesisInfo
from BaseClass.common_task import CommonTask
from SampleData.me_umn import *
from nameparser import HumanName
import re

from utils.connection import extract


class MEUmnClass(ThesisInfo):
    def __init__(self, sec=None, parse_data=None):
        """
        :param sec: item url
        """
        self.sec = sec
        self.parse_data = parse_data
        super(MEUmnClass, self).__init__()
        self.generate_all_method()

    def _generate_avatar(self):
        # regex = '[a-zA-z]+://[^\s]*'
        # res = re.search(regex, str(self.parse_data["avatar"]))
        self.avatar = "http://www.me.umn.edu/people/{}".format(
                              extract(avatar_rule, self.sec))
        
    def _generate_firstName(self):
        if "name" in self.parse_data.keys():
            if self.parse_data["name"]:
                self.firstName = HumanName(self.parse_data["name"]).first
        #self.firstName = HumanName(str(extract(name_rule, self.sec).xpath('string(.)').replace('Faculty Directory',''))).first
    def _generate_lastName(self):
        if "name" in self.parse_data.keys():
            if self.parse_data["name"]:
                self.lastName = HumanName(self.parse_data["name"]).last
        #self.lastName = HumanName(str(extract(name_rule, self.sec).xpath('string(.)').replace('Faculty Directory',''))).last
    
    def _generate_organization(self):
        self.organization = organization
        
    def _generate_major(self):
        self.major = major
        
    def _generate_maincity(self):
        if len(self.city) != 0:
            self.maincity = self.city[0]

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
        else:
            self.website = "http://www.me.umn.edu/people/index.shtml"


    def _generate_keywordKeys(self):
        self.keywordKeys = [i for i in range(1,len(self.keywords)+1)]
    def _generate_cityKeys(self):
        self.cityKeys = [i for i in range(1,len(self.city)+1)]
    def _generate_timeKeys(self):
        self.timeKeys = [i for i in range(1,len(self.timeKeys)+1)]

if __name__ == '__main__':
    MEUmnTask = CommonTask(website_name=MEUmnClass.__name__,
                   custom_parser=MEUmnClass,
                   base_url=base_url,
                   sample_url=sample_url,
                   data=data,
                   item_url_rule=item_url_rule
                   )
    MEUmnTask.run()
