#coding:utf-8
"""
@file:      photo_download
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/20 3:45
@description:
            --
"""


from ErrorHandle.request_error import HTTPError, URLFetchError
from utils.connection import fetch
from utils.logger import get_logger
import requests


def download(url,user_id,logger):
    try:
        tmp = fetch(url,decode=False)
        try:
            with open('../PhotoTemp/{}.jpg'.format(user_id),'wb') as f:
                f.write(tmp)
        except Exception as e:
            logger.warn("{} {} save failed! {}".format(url,user_id,e))
    except Exception as e:
        logger.warn("{} {} download failded! {}".format(url,user_id,e))
        
        
    
if __name__ == '__main__':
    download("http://xiaorui.cc/static/qq_qun2.png",1,get_logger("test"))
    