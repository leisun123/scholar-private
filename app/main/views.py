#coding:utf-8
"""
@file:      views
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/21 4:23
@description:
            --
"""
from wynmail.mail_server import mailjet_api
from . import main
from flask import render_template,jsonify

@main.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@main.route('/info',methods=['GET','POST'])
def show_all_scholars():
    res = mailjet_api.show_all_scholars()
    return render_template("show_all_scholars.html",scholars=res['Data'],count=res['Count'])

@main.route('/contactlist',methods=['GET','POST'])
def show_scholars_contactlist():
    res = mailjet_api.show_scholars_contactlist()
    return render_template("show_scholars_contactlist.html",scholars=res['Data'],count=res['Count'])

@main.route('/recipientstatistic',methods=['GET','POST'])
def show_mail_recipent_static():
    res = mailjet_api.show_mail_recipient_statistic()
    return render_template("show_mail_recipient_statistic.html",scholars=res['Data'],count=res['Count'])
