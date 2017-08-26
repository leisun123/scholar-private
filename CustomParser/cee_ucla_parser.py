#coding:utf-8
"""
@file:      cyber_umd_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-13 下午5:43
@description:
            --
"""
import os
import sys
sys.path.append(os.path.join(os.getcwd().split('scholar')[0],'scholar'))

from BaseModule.ThesisClass import ThesisInfo
from BaseModule.common_task import CommonTask
from SampleData.cee_ucla import *
from nameparser import HumanName
import re

from utils.connection import extract

class CEEUclaClass(ThesisInfo):
    def __init__(self, sec=None, parse_data=None):
        """
        :param sec: item url
        """
        self.sec = sec
        self.parse_data = parse_data
        super(CEEUclaClass, self).__init__()
        self.generate_all_method()

    def _generate_avatar(self):
        if "avatar" in self.parse_data.keys():
            if self.parse_data["avatar"]:
                regex = '[a-zA-z]+://[^\s]*'
                res = re.search(regex, str(self.parse_data["avatar"]))
                self.avatar = res.group()
        self.avatar = extract(avatar_rule, self.sec)
    def _generate_firstName(self):
        if "name" in self.parse_data.keys():
            if self.parse_data["name"]:
                self.firstName = HumanName(extract(name_rule, self.sec).xpath('string(.)').split(',')[1]).first
    def _generate_lastName(self):
        if "name" in self.parse_data.keys():
            if self.parse_data["name"]:
                self.lastName = HumanName(extract(name_rule, self.sec).xpath('string(.)').split(',')[1]).last
    
    def _generate_organization(self):
        self.organization = organization
        
    def _generate_major(self):
        self.major = major
        
    def _generate_title(self):
        if "title" in self.parse_data.keys():
            if self.parse_data["title"]:
                self.title = self.parse_data["title"]
        else:
            self.title = extract(title_rule, self.sec)
    def _generate_maincity(self):
        if len(self.city) != 0:
            self.maincity = self.city[0]

    def _generate_email(self):
        if "email" in self.parse_data.keys():
            if self.parse_data["email"]:
                self.email = self.parse_data["email"]
        else:
            self.email = extract(email_rule, self.sec)
    def _generate_website(self):
        if "website" in self.parse_data.keys():
            if self.parse_data["website"]:
                regex = '"(.*?)"'
                res = re.search(regex, str(self.parse_data["website"]))
                self.website = res.group()
        else:
            self.website = extract(website_rule, self.sec)


    def _generate_keywordKeys(self):
        self.keywordKeys = [i for i in range(1,len(self.keywords)+1)]
    def _generate_cityKeys(self):
        self.cityKeys = [i for i in range(1,len(self.city)+1)]
    def _generate_timeKeys(self):
        self.timeKeys = [i for i in range(1,len(self.timeKeys)+1)]

if __name__ == '__main__':
    # CEEUclaTask = CommonTask(website_name=CEEUclaClass.__name__,
    #                custom_parser=CEEUclaClass,
    #                base_url=base_url,
    #                sample_url=sample_url,
    #                data=data,
    #                item_url_rule=item_url_rule,
    #                default_url="http://www.cee.ucla.edu",
    #                is_url_joint=True
    #                )
    # CEEUclaTask.run()
    pass
