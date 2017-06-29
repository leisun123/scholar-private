from ScholarArticle import ScholarArticle
from decorators import except_pass
from Tool import extract,fetch
from spider_config import RULES
import re

EP_METHOD=lambda func:except_pass(func,ModelName='ScholarArticle')

class ScholarParser(ScholarArticle):
    def __init__(self,sec,ScholarObj):
        self.sec=sec
        ScholarArticle.__init__(self,ScholarObj)
        self.generate_all_method()
        self.insertdb()

    @EP_METHOD
    def generate_title(self):
        self.title=extract(RULES["title"],self.sec)
    @EP_METHOD
    def generate_author(self):
        self.author=extract(RULES["author"],self.sec)
    @EP_METHOD
    def generate_url(self):
        self.url=extract(RULES["url"],self.sec)
    @EP_METHOD
    def generate_email(self):
        temp=extract(RULES["email"],self.sec)
        # self.email=temp.split(':')[1]
        emailRegex = r"([\w\.\-]+@[\w\.\-]+)"
        self.email = re.search(emailRegex,str(temp).replace(' ','')).group(0)