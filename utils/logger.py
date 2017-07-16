#coding:utf-8
"""
@file:      logger
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2017-03-03 20:59
@description:
            --
"""
import logging
def get_logger(name):
    """logger
    """
    default_logger = logging.getLogger(name)
    default_logger.setLevel(logging.DEBUG)
    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
    stream.setFormatter(formatter)
    default_logger.addHandler(stream)
    return default_logger

