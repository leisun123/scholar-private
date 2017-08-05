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
        self.city = ["China"]
        self.time = ["Flexible"]
        self.keywordKeys = []
        self.cityKeys = [1]
        self.timeKeys = [1]

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
        
        parm = {
                "name":"{} {}".format(self.firstName,self.lastName),
                "email":self.email,
                "password":"bcrypt",
                "avatar":self.avatar,
                "profile":
                    {
                    "keywordKeys":self.keywordKeys,
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
                    "bio":self.bio
                    }
                }
        for i in self.keywordKeys:
            parm["profile"]["keyword-{}".format(i)] = self.keywords[i-1]
        for j in self.cityKeys:
            parm["profile"]["city-{}".format(j)] = self.cityKeys[j-1]
        for h in self.timeKeys:
            parm["profile"]["time-{}".format(h)] = self.timeKeys[h-1]
        return parm
        
        
        
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
    parm = {"keywordKeys":[1,2,3],
            "cityKeys":[1],
            "timeKeys":[1],
            "firstName":"Chun-Hung",
            "lastName":"Chen",
            "organization":"George Mason University",
            "major":"System Engineering",
            "title":"Professor",
            "birth":"2017-05-30",
            "country":"USA",
            "state":"VA",
            "city":"Fairfax",
            "phone":"+1 (703) 993-3572",
            "email":"cchen9@gmu.edu",
            "website":"http://mason.gmu.edu/~cchen9/",
            "cooperation":["Short time teaching","Customizing core curriculum","Research or development"],
            "bio":"Understanding what could go wrong before it happens is vital to almost every industry. Stochastic modeling works to help engineers simulate incidents that arise from seemingly random circumstances. This is especially important to air transportation systems, technology manufacturing, healthcare, security networks, power grids, and military operations. Chun-\n\nHung Chen is the inventor of a novel idea called Optimal Computing Budget Allocation, which drastically improves the efficiency of stochastic simulation. Because this methodology has proven to be of great importance to so many applications, Chen鈥檚 research has been funded by a variety of organizations such as the National Science Foundation, the National Institutes of Health, the Department of Energy, NASA, the US Air Force, the US Missile Defense Agency, and the Federal Aviation Administration. Chen teaches several sections of systems simulation modeling and research techniques on the graduate and undergraduate level.\n",
            "keyword-1":"highly efficient methodology ",
            "keyword-2":"semiconductor manufacturing",
            "keyword-3":"power grids",
            "city-1":"China",
            "time-1":"Flexible"}
    pass
    
    