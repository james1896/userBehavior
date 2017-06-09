# -*- coding: utf-8 -*-

# 配置数据库
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:123456@127.0.0.1:3306/test?charset=utf8",
                       encoding="utf-8",
                       echo=False)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
import mysql.model

Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)