#coding:utf-8
"""
@file:      scholar_info_spider
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 2:16
@description:
            --
"""
import requests
class ThesisInfo(object):
    def __init__(self):
        self.avatar = None
        self.firstName = None
        self.lastName = None
        self.organization = None
        self.major = None
        self.title = None
        self.birth = None
        self.country = None
        self.state = None
        self.maincity = None
        self.phone = None
        self.email = None
        self.website = None
        self.cooperation = []
        self.bio = None
        self.keywords = []
        self.city = []
        self.time = []
        self.keywordKeys = []
        self.cityKeys = []
        self.timeKeys = []

    def _generate_avatar(self):
        pass
    def _generate_firstName(self):
        pass
    def _generate_lastName(self):
        pass
    def _generate_organization(self):
        pass
    def _generate_major(self):
        pass
    def _generate_title(self):
        pass
    def _generate_birth(self):
        pass
    def _generate_country(self):
        pass
    def _generate_state(self):
        pass
    def _generate_maincity(self):
        pass
    def _generate_phone(self):
        pass
    def _generate_email(self):
        pass
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
        pass
    def _generate_cityKeys(self):
        pass
    def _generate_timeKeys(self):
        pass
    
    def generate_all_method(self):
        self._generate_avatar()
        self._generate_firstName()
        self._generate_lastName()
        self._generate_organization()
        self._generate_major()
        self._generate_title()
        self._generate_birth()
        self._generate_country()
        self._generate_state()
        self._generate_city()
        self._generate_phone()
        self._generate_email()
        self._generate_website()
        self._generate_cooperation()
        self._generate_bio()
        self._generate_keywords()
        self._generate_maincity()
        self._generate_time()
        self._generate_keywordKeys()
        self._generate_cityKeys()
        self._generate_timeKeys()
    

            
    def set_value(self):
        
        return {
                "name":"{} {}".format(self.firstName,self.lastName),
                "email":self.email,
                "password":"bcrypt",
                "avatar":self.avatar,
                "profile":
                    {"keywordKeys":self.keywordKeys,
                    "cityKeys":self.cityKeys,
                    "timeKeys":self.timeKeys,
                    "firstName":self.firstName,
                    "lastName":self.lastName,
                    "organization":self.organization,
                    "major":self.major,
                    "title":self.title,
                    "birth":self.birth,
                    "country":self.country,
                    "state":self.state,
                    "city":self.city,
                    "phone":self.phone,
                    "email":self.email,
                    "website":self.website,
                    "cooperation":self.cooperation,
                    "bio":self.bio,
                    "keywords":self.keywords,
                    "city":self.city,
                    "time":self.time
                    }
                }
        
    def terminal_monitoring(self):
        print('*******************scholar info***********************')
        print('avatar:\t\t{}'.format(self.avatar))
        print('firstName:\t\t{}'.format(self.firstName))
        print('lastName:\t\t{}'.format(self.lastName))
        print('organization:\t\t{}'.format(self.organization))
        print('major:\t\t{}'.format(self.major))
        print('title:\t\t{}'.format(self.title))
        print('birth:\t\t{}'.format(self.birth))
        print('country:\t\t{}'.format(self.country))
        print('state:\t\t{}'.format(self.state))
        print('city:\t\t{}'.format(self.maincity))
        print('phone:\t\t{}'.format(self.phone))
        print('email:\t\t{}'.format(self.email))
        print('website:\t\t{}'.format(self.website))
        print('cooperation:\t\t{}'.format(self.cooperation))
        print('bio:\t\t{}'.format(self.bio))
        print('keywords:\t\t{}'.format(self.keywords))
        
if __name__ == '__main__':
    print(ThesisInfo.__dict__)