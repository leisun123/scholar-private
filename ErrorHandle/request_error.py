#coding:utf-8
"""
@file:      net_error
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 3:03
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