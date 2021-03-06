#-*-coding:utf-8-*-

from utils.connection import *
from utils.set_value import *

def get_data(url):
    res = fetch(url)
    tmp = extract("//div[@class='directory-entry col-sm-4 col-md-3 col-lg-3']",res,multi=True)
    for a in tmp:
        name = extract("//*[@class='name']/b/text()",html_source=str(etree.tostring(a)))
        email = extract("//*[@class='email']/text()",html_source=str(etree.tostring(a)))
        web = extract("//a/@href", str(etree.tostring(a)))
        avtar = extract("//a/img/@src",str(etree.tostring(a)))
        organization = "University of North Carolina"
        major = "Department of Civil, Construction, and Environmental Engineering"
        print(set_value(name,email,web,organization,major,avtar))

get_data("https://www.ccee.ncsu.edu/faculty-staff/")