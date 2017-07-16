#coding:utf-8
"""
@file:      science_direct
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 2:44
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
from ScholarConfig.europepmc_rule import RULES
PS_ERROR = lambda func:except_pass(func,ModelName = 'ScienceDirect')

class ScienceDirect(ThesisInfo):
    def __init__(self,sec):
        """
        :param sec: item url
        """
        self.sec = sec
        super(ScienceDirect, self).__init__()
        self.generate_all_method()
        # parm=self.set_value()
        # sqlhelper=SqlHelper()
        # sqlhelper.insert_scholar_thesis(**parm)
        
    @PS_ERROR
    def _generate_title(self):
       self.title=extract(RULES["title"],self.sec)
    
    @PS_ERROR
    def _generate_source_url(self):
        self.url=extract(RULES["source_url"],self.sec)
    
    @PS_ERROR
    def _generate_keywords(self):
        pass
    
    @PS_ERROR
    def _generate_update_time(self):
        import time
        self.update_time = datetime.utcnow()
    
    @PS_ERROR
    def _generate_publish_time(self):
        self.publish_time = extract(RULES["publish_time"],self.sec)
    
    @PS_ERROR
    def _generate_abstract(self):
        self.abstract = extract(RULES["abstract"],self.sec)
        
    @PS_ERROR
    def _generate_type(self):
        self.type = extract(RULES["type"],self.sec)
        
    @PS_ERROR
    def _generate_doi(self):
        self.doi = extract(RULES["doi"],self.sec)
    
    @PS_ERROR
    def _generate_pdf_url(self):
        if "PDF" in self.sec:
            self.pdf_url = extract(RULES["pdf_url"],self.sec)
        else:
            self.pdf_url = None
    @PS_ERROR
    def _generate_scholar_info(self):
        tmp = extract(RULES["scholar_info_list"],self.sec,multi=True)
        for i in tmp:
            name=extract(RULES["author_name"],str(etree.tostring(i)))
            affiliation=extract(RULES["affiliation"],str(etree.tostring(i)))
            emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
            a=re.search(emailRegex,str(affiliation).replace(' ',''))
            if a is not None:
                email=a.group(0)
            else:
                email=None
            if affiliation is not None:
                m=affiliation.split(',')
                profession=m[0]
                university=m[1]
                city=m[2]
                country=m[3]
            else:
                profession=None
                university=None
                city=None
                country=None
            self.scholar_info.append({"name":name,"email":email,"profession":profession,"university":university,"city":city,"country":country})
            
    
    

    
    
    
        