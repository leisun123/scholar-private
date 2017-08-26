#coding:utf-8
"""
@file:      science_direct_parser
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/8/17 19:56
@description:
            --
"""

from BaseModule.ThesisClass import ThesisInfo
from ErrorHandle.parse_error import except_pass

PS_ERROR = lambda func:except_pass(func,ModelName = 'science_direct')

class ScienceDirectClass(ThesisInfo):
    def __init__(self, sec, webdriver):
        """
        :param sec: item url
        """
        self.sec = sec
    
        super(ScienceDirectClass, self).__init__()
        self.driver = webdriver
        self.driver.get(self.sec)
        self.scholar_list = self.driver.find_elements_by_xpath("//div[@class='author-group']/a")
        
    @PS_ERROR
    def _parser_data(self):
        for scholar in self.scholar_list:
            try:
                scholar.click()
                self.email = self.driver.find_element_by_xpath("//div[@class='e-address']").\
                    text.replace('Opens the author workspace','').strip()
                
                self.firstname = self.driver.find_element_by_xpath("//div[@class='author']/span[1]").text
        
                self.lastname = self.driver.find_element_by_xpath("//div[@class='author']/span[2]").text
                
                try:
                     affiliation = self.driver.find_element_by_xpath("//div[@class='affiliation']").text
                     self.major = affiliation.split(',')[0].replace('Corresponding authors at:','').\
                         replace('Opens the author workspace','').\
                         replace('Corresponding author.','').\
                         replace('Corresponding author at:','').\
                         strip()
                     for i in affiliation.split(','):
                         if 'University' or 'university'in i:
                             self.organization = i.replace('Corresponding author at:','').strip()
                except:
                    try:
                        correspondence = self.driver.find_element_by_xpath("//div[@class='correspondence']").text
                        self.major = correspondence.split(',')[0].replace('Corresponding authors at:','').\
                            replace('Opens the author workspace','').\
                            replace('Corresponding author.','').\
                            replace('Corresponding author at:','').\
                            strip()
                        for i in affiliation.split(','):
                            if 'University' or 'university' in i:
                                self.organization = i.replace('Corresponding author at:','').strip()
                    except:
                        self.logging.warning('Cardiac plug plug, major or organzization got none (┬＿┬).......')
            except:
                self.logging.error('大学之道在明明德，在亲民，在止于至善。')
            
if __name__ == '__main__':
    pass