#coding:utf-8
"""
@file:      SqlHelper
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/6/29 23:12
@description:
            --
"""
import datetime
from sqlalchemy import Column,Integer,String,DateTime,Numeric,create_engine,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ScholarConfig.config import DB_CONFIG

from db.ISqlHelper import ISqlHelper

BaseModel = declarative_base()

class ThesisBase(BaseModel):
    __tablename__='thesis'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(VARCHAR(500),nullable=False)
    source_url = Column(VARCHAR(500))
    keywords = Column(VARCHAR(500))
    update_time= Column(DateTime(),default=datetime.datetime.utcnow)
    publish_time =Column(VARCHAR(200))
    abstract = Column(VARCHAR(3000))
    type = Column(VARCHAR(100))
    doi = Column(VARCHAR(100))
    pdf_url = Column(VARCHAR(500))
    
    
class ScholarBase(BaseModel):
    __tablename__='scholar'
    id = Column(Integer,primary_key=True,autoincrement=True)
    thesis = Column(VARCHAR(200))
    name = Column(VARCHAR(200),nullable=False)
    last_name = Column(VARCHAR(50),nullable=False)
    email = Column(VARCHAR(300))
    profession = Column(VARCHAR(300))
    university = Column(VARCHAR(200))
    city = Column(VARCHAR(200))
    country = Column(VARCHAR(200))
    affiliation = Column(VARCHAR(1000))
  
class Proxy(BaseModel):
    __tablename__ = 'proxys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(VARCHAR(16), nullable=False)
    port = Column(Integer, nullable=False)
    types = Column(Integer, nullable=False)
    protocol = Column(Integer, nullable=False, default=0)
    country = Column(VARCHAR(100), nullable=False)
    area = Column(VARCHAR(100), nullable=False)
    updatetime = Column(DateTime(), default=datetime.datetime.utcnow)
    speed = Column(Numeric(5, 2), nullable=False)
    score = Column(Integer, nullable=False, default=10)
    
    
class SqlHelper(ISqlHelper):
    def __init__(self):
        if 'sqlite' in DB_CONFIG['DB_CONNECT_STRING']:
            connect_args = {'check_same_thread':False}
            self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'],echo=False,connect_args=connect_args)
        else:
            self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'],echo=False)
        DB_Session = sessionmaker(bind=self.engine)
        self.session = DB_Session()
        
    def init_db(self):
        BaseModel.metadata.create_all(self.engine)
        
    def drop_db(self):
        BaseModel.metadata.drop_all(self.engine)
        
    def insert_scholar_thesis(self, **values):
        thesis = ThesisBase(
                              title=values['title'],
                              source_url=values['source_url'],
                              keywords=values['keywords'],
                              update_time=values['update_time'],
                              publish_time=values['publish_time'],
                              abstract=values['abstract'],
                              type=values['type'],
                              doi=values['doi'],
                              pdf_url=values['pdf_url']
                              )
        from nameparser import HumanName
        for i in values['scholar_info']:
            scholar = ScholarBase(
                              name=i['name'],
                              last_name=HumanName(i['name']).last,
                              thesis=values['title'],
                              email=i['email'],
                              profession=i['profession'],
                              university=i['university'],
                              city=i['city'],
                              country=i['country']
                                )
            self.session.add(scholar)
        self.session.add(thesis)
        self.session.commit()
        
    def output_proxy(self):
        ipprort=self.session.query(Proxy.ip,Proxy.port).all()
        with open("../utils/1.txt","r+") as f:
             for i,j in ipprort:
                 f.writelines("{}:{}\n".format(i.replace('\'',''),j))
                
    def delete(self, conditions=None):
        if conditions:
            condition_list = []
            for key in list(conditions.keys()):
                if self.params.get(key,None):
                    condition_list.append(self.params.get(key)==conditions.get(key))
            conditions = condition_list
            query = self.session.query(ThesisBase)
            for condition in conditions:
                query = query.filter(condition)
            deleteNum = query.delete()
            self.session.commit()
        else:
            deleteNum = 0
        return {'deleteNum',deleteNum}
    
    def update(self, conditions=None,value=None):
        pass
    
    def select(self, count=None,conditions=None):
        pass
    
    def close(self):
        pass
    
if __name__ == '__main__':
    sqlhelper = SqlHelper()
    import time
    from datetime import datetime
    # sqlhelper.drop_db()
    # sqlhelper.init_db()
    sqlhelper.output_proxy()
        
        
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    