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
from sqlalchemy import *
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from ScholarConfig.config import DB_CONFIG,create_ssh_tunnel
import simplejson
from db.ISqlHelper import ISqlHelper
from uuid import uuid4

from utils.logger import get_logger
from utils.photo_download import download

BaseModel = declarative_base()


class Group(BaseModel):
    __tablename__ = 'groups'

    id = Column(BigInteger, primary_key=True)
    object_id = Column(String(36), nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    
class ObjectAttribute(BaseModel):
    __tablename__ = 'object_attributes'
    __table_args__ = (
        Index('object_id', 'object_id', 'name', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    object_id = Column(String(36), nullable=False)
    name = Column(String(255), nullable=False)
    value = Column(LargeBinary)


class Object(BaseModel):
    __tablename__ = 'objects'

    id = Column(String(36), primary_key=True, unique=True)
    parent = Column(String(36))
    type = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    object_id = Column(String(36), nullable=False)
    scope = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    reset_password_token = Column(Text)
    reset_password_sent_at = Column(DateTime)
    remember_created_at = Column(DateTime)
    sign_in_count = Column(BigInteger, nullable=False, server_default=text("'0'"))
    current_sign_in_at = Column(DateTime)
    last_sign_in_at = Column(DateTime)
    current_sign_in_ip = Column(Text)
    last_sign_in_ip = Column(Text)
    confirmation_token = Column(Text)
    confirmed_at = Column(DateTime)
    confirmation_sent_at = Column(DateTime)
    unconfirmed_email = Column(Text)
    failed_attempts = Column(Integer, nullable=False, server_default=text("'0'"))
    unlock_token = Column(Text)
    locked_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class UserGroup(BaseModel):
    __tablename__ = 'user_groups'
    __table_args__ = (
        Index('unique_user_id_group_id', 'user_id', 'group_id', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    group_id = Column(ForeignKey('groups.id'), nullable=False, index=True)
    group = relationship('Group')
    user = relationship('User')
    
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
    def __init__(self,logger=None):
        self.logger = logger
        if 'sqlite' in DB_CONFIG['DB_CONNECT_STRING']:
            connect_args = {'check_same_thread':False}
            self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'],echo=False,connect_args=connect_args)
        else:
            #self.engine =create_ssh_tunnel()
            self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'])
            DB_Session = sessionmaker(bind=self.engine)
            self.session = DB_Session()
        
    def init_db(self):
        BaseModel.metadata.create_all(self.engine)
        

    def drop_db(self):
        BaseModel.metadata.drop_all(self.engine)
    
        
    def insert_scholar(self, **values):
        tmp_id = str(uuid4())
        tmp_create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        object = Object(
                        id = tmp_id,
                        parent = None,
                        type = "user",
                        name = "User:{}".format(tmp_id),
                        created_at = tmp_create_time
                        )
        
        user = User(
                        object_id = tmp_id,
                        scope = "",
                        name = values["name"],
                        email = values["email"],
                        password = "bcrypt",
                        reset_password_token = None,
                        reset_password_sent_at = None,
                        remember_created_at = None,
                        
                        current_sign_in_at = None,
                        last_sign_in_at = None,
                        current_sign_in_ip = None,
                        last_sign_in_ip = None,
                        confirmation_token = None,
                        confirmed_at = None,
                        confirmation_sent_at = None,
                        unconfirmed_email = None,
                        
                        unlock_token = None,
                        locked_at = None,
                        created_at = tmp_create_time,
                        updated_at = None
        )
        
        object_attributes_profile = ObjectAttribute(
                        object_id = tmp_id,
                        name = "profile",
                        value = bytes(simplejson.dumps(values["profile"]),encoding='utf8'))


        object_attributes_password = ObjectAttribute(
                        object_id = tmp_id,
                        name = "password",
                        value = bytes(values["password"],encoding='utf8')
        )

        

        try:
            self.session.add(object)
            self.session.add(object_attributes_profile)
            self.session.add(object_attributes_password)
            self.session.add(user)
            self.session.flush()
            object_attributes_avatar = ObjectAttribute(
                        object_id = tmp_id,
                        name = "avatar",
                        value = bytes("{}.jpg".format(user.id),encoding='utf8')
                        )
            user_group = UserGroup(
                        user_id = user.id,
                        group_id = 5
                        )
            self.session.add(object_attributes_avatar)
            self.session.add(user_group)
            download(values["avatar"],user.id,self.logger)
            self.logger.info("{} has inserted".format(user.name))
            self.session.commit()
        except exc.SQLAlchemyError as e:
            self.logger.error("{} info commit failed! Caused by {}".format(values["name"],e))
            self.session.rollback()

    
    def output_proxy(self):
        ipprort=self.session.query(Proxy.ip,Proxy.port).all()
        with open("../utils/1.txt","r+") as f:
             for i,j in ipprort:
                 f.writelines("{}:{}\n".format(i.replace('\'',''),j))
    
    #生产库慎用
    def parser_data_delete(self):
        result = iter(self.session.query(User).outerjoin(UserGroup,User.password.like("bcr%")).all())
        try:
            while True:
                i = next(result)
                try:
                    self.session.query(Object.id)
                    self.session.query(Object).filter(Object.id == i.object_id).delete()
                    self.session.query(ObjectAttribute).filter(ObjectAttribute.object_id == i.object_id).delete()
                    self.session.query(UserGroup).filter(UserGroup.user_id == i.id).delete()
                    self.session.query(User).filter(User.id ==  i.id).delete()
                    self.session.commit()
                    self.logger.info("deleted {}".format(i.name))
                except exc.SQLAlchemyError as e:
                    self.logger.error("{} delete fail! Caused by{}".format(i.id,e))
                    self.session.rollback()
        except StopIteration:
            self.logger.info("Finish")
        self.session.close()
    
    def update(self, conditions=None,value=None):
        pass
    
    def select(self, count=None,conditions=None):
        pass
    
    def close(self):
        pass
    
if __name__ == '__main__':
    sqlhelper = SqlHelper(logger=get_logger("test"))
    sqlhelper.parser_data_delete()
    
    
        
        
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    