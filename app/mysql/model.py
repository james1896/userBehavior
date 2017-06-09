# -*- coding: utf-8 -*-
# #########################   User表结构    #####################################################
from sqlalchemy import Column, Integer, String, Float, DateTime, VARCHAR, ForeignKey
from app.config import Base
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    pwd = Column(String(120), unique=False)
    user_id = Column(String(40), unique=True)
    email = Column(String(120), unique=False)
    points = Column(Float, unique=False)
    first_time = Column(DateTime,unique=False)

    status = Column(Integer, unique=False)
    uuid = Column(String(120), unique=False)
    device = Column(String(50), unique=False)


    def __init__(self, name=None,pwd=None,user_id=None):
        self.name       = name
        self.pwd        = pwd
        self.user_id    = user_id
        self.email      = None
        self.points     = 0.0
        self.first_time  = None

        self.status     = 0
        self.uuid       ='uuid'
        self.device     ='device'

    def __repr__(self):
        return '%s (%r, %r)' % (self.__class__.__name__, self.name, self.email)


# #########################   用户行为统计    #####################################################

class table_behavior_log(Base):
    __tablename__ = 't_behavior_log'

    id      = Column(Integer, primary_key=True)
    # user_id = Column(VARCHAR(20),)
    func_id = Column(Integer, unique=False)
    begin_time = Column(DateTime, unique=False)
    duration = Column(Integer, unique=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self,user_id=None):
        self.user_id = user_id

#  用户行为历史记录
# （每天同步用户行为记录）

class table_history_behavior_log(Base):
    __tablename__ = 't_history_behavior_log'
    id = Column(Integer, primary_key=True)
    func_id = Column(Integer, unique=False)
    begin_time = Column(DateTime, unique=False)
    duration = Column(Integer, unique=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, user_id=None):
        self.user_id = user_id


 # report_type
 # 统计类型：按天统计  按月统计 按年统计

class table_report(Base):
    __tablename__ = 't_report'

    id = Column(Integer, primary_key=True)
    func_id = Column(Integer, unique=False)
    report_type = Column(Integer, unique=False)
    duration = Column(Integer, unique=False)


    user_id = Column(Integer, ForeignKey('users.id'))

    # 上面的字段需要改成下面的
    # id, type,         time,   user_count, monetary
    #   统计类型(小时／天) 时间     用户数量     消费

