# coding:utf-8
"""
@file:      Doubanclass
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2017-03-04 21:34
@description:
            --
"""

from logger import logger
import psycopg2

from gevent.pool import Pool
from gevent.queue import Queue
from spider_config import *


class Scholar(object):
    def __init__(self):
        self.entrance_url_list=ENTRANCE_URL_LIST

        self.interval = WATCH_INTERVAL

        self.pool = Pool(size=POOL_SIZE)
        self.page_queue = Queue()
        self.info_queue = Queue()

    def connectdb(self):
        try:
            self.conn = psycopg2.connect(database="scholar",
                                         user="wyn",
                                         password="weiaizq1314",
                                         host="127.0.0.1",
                                         port="5432")

            return self.conn
        except psycopg2.Error as e:
            logger.warn(e)

    def closedb(self):
        self.conn = self.connectdb()
        self.conn.close()


if __name__ == '__main__':
    d = Scholar()
    cur = d.connectdb().cursor()
    cur.execute("select count(*) from scholar")
    print(cur.fetchall())






















