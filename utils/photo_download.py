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

from gevent import monkey
monkey.patch_all()
import gevent
from gevent.pool import Pool
from gevent.queue import Queue
from ErrorHandle.request_error import HTTPError, URLFetchError
from ErrorHandle.file_save_error import FileSaveError
from utils.logger import get_logger
import requests

def PhotoDownload(website,photo_id):
    logger = get_logger(website)
    download_queue = Queue()
    def download():
        download_pool = Pool(size=20)
        nonlocal  logger
        nonlocal download_queue
        try:
            url = download_queue.get(block=True)
            resp = requests.get(url)
            if resp.status_code != 200:
                raise HTTPError(resp.status_code,url)
            try:
                with open('./PhotoTemp/{}'.format(photo_id),'w+') as f:
                    f.write(resp.content)
            except Exception as e:
                logger.warn("{} {} save failed! {}".format(website,photo_id,e))
        except Exception as e:
            logger.warn("{} {} download failded! {}".format(url,photo_id,e))
        
        
    
    
    