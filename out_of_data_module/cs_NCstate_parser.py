#-*-coding:utf-8-*-

from utils.connection import *
from utils.set_value import *

def get_data(url):
    res = fetch(url)
    tmp = extract("//div[@class='person col-lg-5 col-xs-4']",res,multi=True)
    for a in tmp:
        name = extract("//*[@class='speaker']/a/text()",html_source=str(etree.tostring(a))).replace('Dr.  ','').replace('  ','')
        email = extract("//*[@class='info']//*[contains(text(), ' AT ')]/text()",html_source=str(etree.tostring(a)))
        if email is not None:
            email=email.replace(' AT ','@')
        web = "https://www.csc.ncsu.edu" + extract("//a/@href", str(etree.tostring(a)))
        organization = "University of North Carolina"
        major = "Department of Computer Science"
        avatar = "https://www.csc.ncsu.edu" + extract("//*[@class='person_img']/@src",str(etree.tostring(a)))
        print(set_value(name,email,web,organization,major,avatar))

get_data("https://www.csc.ncsu.edu/directories/faculty.php")