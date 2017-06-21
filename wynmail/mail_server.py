# coding:utf-8
"""
@file:      mail-server
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/19 4:23
@description:
            --
"""

from wynmail.MailjetApi import MailjetApi


mailjet_api = MailjetApi(user="7f4b179a5a852eb66eadfc48a95e9aa6",
                         password="381eecab9ebccdc9d4895f4392b78284")


    # a = mailjet_api.send_email(fromm = "genius_wz@aliyun.com",
    #                        to = "1178180942@qq.com",
    #                        subject = "11",
    #                        message = "113")
# with open('1.csv') as f:
#     f_csv = csv.DictReader(f)
#     for row in f_csv:
#         print(row['email'],row['name'])
#         print(mailjet_api.create_contact(email=row['email'],name=row['name']))
#
#
#
# # contactlist_id=mailjet_api.get_apiKey(id=580767)
# # print(contactlist_id)
#print(mailjet_api.view_contactlist())
#print(mailjet_api.show_scholar_contactlist())
#res=mailjet_api.show_mail_recipient_static()
