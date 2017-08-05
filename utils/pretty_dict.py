#coding:utf-8
"""
@file:      pretty_dict
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/22 3:07
@description:
            --
"""
def pretty_dict(obj, indent=' '):
    def _pretty(obj, indent):
        for i, tup in enumerate(obj.items()):
            k, v = tup
            #如果是字符串则拼上""
            if isinstance(k, str): k = '"%s"'% k
            if isinstance(v, str): v = '"%s"'% v
            #如果是字典则递归
            if isinstance(v, dict):
                v = ''.join(_pretty(v, indent + ' '* len(str(k) + ': {')))#计算下一层的indent
            #case,根据(k,v)对在哪个位置确定拼接什么
            if i == 0:#开头,拼左花括号
                if len(obj) == 1:
                    yield '{%s: %s}'% (k, v)
                else:
                    yield '{%s: %s,\n'% (k, v)
            elif i == len(obj) - 1:#结尾,拼右花括号
                yield '%s%s: %s}'% (indent, k, v)
            else:#中间
                yield '%s%s: %s,\n'% (indent, k, v)
    print((''.join(_pretty(obj, indent))))
    
if __name__ == '__main__':
    d = {"name":"Narendra Ahuja",
"email":"n-ahuja@illinois.edu",
"password":"bcrypt",
"avatar":"http://ws.engr.illinois.edu/directory/viewphoto.aspx?id=30761&s=215&type=portrait",
"profile":{"keywordKeys":[1],
"cityKeys":[1],
"timeKeys":[1],
"firstName":"Narendra",
"lastName":"Ahuja",
"organization":"University of Illinois",
"major":"Algorithms and computational complexity",
"title":"Professor Emeritus",
"birth":"",
"country":"USA",
"state":"Illinois",
"city":"Urbana",
"phone":"(217) 333-1837",
"email":"n-ahuja@illinois.edu",
"website":"http://vision.ai.uiuc.edu/ahuja.html",
"cooperation":[],
"bio":"Teaching courses on Computer Vision, Pattern Recognition, Computer Engineering, Probability Theory, Robotics, and Knowledge Networks. In the last few years, co-developed two new interdisciplinary courses with colleagues from other departments: (1) Visualizing and Navigating Knowledge Networks. Co-developed with Profs. N. Contractor of Dept. of Speech Communication and Prof. M. Twidale of School of Library and Information Science. Under Madden Grant, awarded by UIUC Chancellors office. Taught twice. (2) Image Structure, Content and Depiction. Co-developed with Prof. P. Dhillon of Dept. of Educational Policy Studies. Being taught in Spring 2008. (1) Introduced a new computational approach to automatically extracting syntax of images, and using it for automated image understanding. We introduced automated ways of discovering, modeling, recognizing and explaining object categories occurring in arbitrary image sets without supervision and automatically organizing these categories into taxonomies. (2) Introduced a novel, Fourier based formulation for representation and synthesis of videos of dynamic textures. Conventionally, dynamic textures have been analyzed only in spatial domain. Undergraduate student can participate in research projects in the areas of computer vision, pattern recognition, human computer interaction, novel cameras and image and video retrieval.","keyword":["Algorithms and computational complexity"],
"city":["china"],
"time":["flexible"]}}
pretty_dict(d)
    