#coding:utf-8
"""
@file:      Error
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2017-03-03 20:57
@description:
            --
"""
class HTTPError(Exception):

    """ HTTP状态码不是200异常 """

    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return "%s HTTP %s" % (self.url, self.status_code)


class URLFetchError(Exception):

    """ HTTP请求结果为空异常 """

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "%s fetch failed!" % self.self.url