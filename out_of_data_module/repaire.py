from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
import os
import pymysql




# def dele():#删除文件中已经入库得链接
#     if os.path.exists('./new_url.txt'):
#         os.remove('./new_url.txt')
#     with SSHTunnelForwarder(
#     ('39.104.50.183',22),
#     ssh_username = "sc",
#     ssh_pkey="./id_rsa",
#     remote_bind_address=('127.0.0.1',5432)
#     ) as server:
#         server.start()
#         engine = create_engine('postgresql://wyn:weiaizq1314@127.0.0.1:{}/sc_2018'.format(server.local_bind_port))
#         Session = sessionmaker(bind=engine)
#         session = Session()
#         sql = '''SELECT pdf FROM paper'''
#         rows = session.execute(sql)
#         session.commit()
#         session.close()
#         list = []
#         file = []
#         for i in rows:
#             if '/pdf' in i:
#                 list.append("/science/article/pii/"+i[0].split('/pdf')[0].split('pii/')[-1])
#             else:
#                 list.append("/science/article/pii/"+i[0].split('&origin')[0].split('s2.0-')[-1].split('-main.pdf')[0])
#         print(list)
#         with open('./url.txt','r') as f:
#             lines = f.readlines()
#             for line in lines:
#                 file.append(line.split('\n')[0])
#             f.close()
#         # with open('./TODO.txt','r') as f:
#         #     lines =f.readlines()
#         #     for line in lines:
#         #         file.append(line.split('com')[-1].split('\n')[0])
#         newlist = set(file)-set(list)
#         print(len(set(file)),len(set(list)),len(newlist))
#         print(len(file))
#         with open('./new_url.txt','a') as f:
#             for i in newlist:
#                 f.write(i+'\n')
#             f.close()
#         # if os.path.exists('./TODO.txt'):
#         #     os.remove('./TODO.txt')
#         # os.remove('./new_url.txt')
#         # os.remove('./new_url.txt')
with SSHTunnelForwarder(
    ('123.206.116.125',22),
    ssh_username = "ubuntu",
    ssh_password="yb123456",
    remote_bind_address=('127.0.0.1',3306)
    ) as server:
    server.start()
    print(server.local_bind_port)
    myConfig = pymysql.connect(
        charset='utf8',
        user="root",
        password="yb123456",
        host="localhost",
        db='calendar',
        port=server.local_bind_port,
        cursorclass=pymysql.cursors.DictCursor)
    my_cousor = myConfig.cursor()
        # engine = create_engine('mysql://root:123456@127.0.0.1:{}/calender'.format(server.local_bind_port))
        # Session = sessionmaker(bind=engine)
        # session = Session()
    # sql = '''show tables;'''
    sql_select = 'SELECT * FROM event;'
    # 用一个变量接收mysql语句
    my_cousor.execute(sql_select)
    # 执行
    my_cousor.rowcount
    # 返回被execute影响的数据的行数,注：execute不是方法.
    get_row = my_cousor.fetchall()
    # 取结果集剩下所有行
    for i in get_row:
        print(i)
    myConfig.commit()
        # rows = session.execute(sql)
        # session.commit()
        # session.close()