# -*- coding: utf-8 -*-

import datetime
import random
import time

from app import db_session
from app.mysql.model import User, table_behavior_log, table_history_behavior_log

def getYesterday():
	today=datetime.date.today()
	oneday=datetime.timedelta(days=1)
	yesterday=today-oneday
	return yesterday

def test():
    print getYesterday()
    ontime_list = [str(getYesterday()) + " 00:00:00",
                   str(getYesterday()) + " 01:00:00",
                   str(getYesterday()) + " 02:00:00",
                   str(getYesterday()) + " 03:00:00",
                   str(getYesterday()) + " 04:00:00",
                   str(getYesterday()) + " 05:00:00",
                   str(getYesterday()) + " 06:00:00",
                   str(getYesterday()) + " 07:00:00",
                   str(getYesterday()) + " 08:00:00",
                   str(getYesterday()) + " 09:00:00",
                   str(getYesterday()) + " 10:00:00",
                   str(getYesterday()) + " 11:00:00",
                   str(getYesterday()) + " 12:00:00",
                   str(getYesterday()) + " 13:00:00",
                   str(getYesterday()) + " 14:00:00",
                   str(getYesterday()) + " 15:00:00",
                   str(getYesterday()) + " 16:00:00",
                   str(getYesterday()) + " 17:00:00",
                   str(getYesterday()) + " 18:00:00",
                   str(getYesterday()) + " 19:00:00",
                   str(getYesterday()) + " 20:00:00",
                   str(getYesterday()) + " 21:00:00",
                   str(getYesterday()) + " 22:00:00",
                   str(getYesterday()) + " 23:00:00"]
    for i in range(0,len(ontime_list)):
        first = ontime_list[i]
        second = None
        if i != len(ontime_list)-1:
            second = ontime_list[i+1]
        else:
            second = ontime_list[0]
        print 'first:',first," - second:",second


    # print db_session.query(table_behavior_log).filter(table_behavior_log.begin_time.between("2017-06-08 11:00:00","2017-06-08 12:00:00")).count()

def test01():
  print  db_session.query(table_history_behavior_log).filter(table_history_behavior_log.begin_time.like('%s '%(getYesterday())+'%')).all()

def timingSyncData():
    # behaviors = db_session.query(table_behavior_log).all()
    # 每晚凌晨2点同步数据
    # 查询到前一天所有的记录
    #
    behaviors = db_session.query(table_behavior_log).filter(table_behavior_log.begin_time.like('%s ' % (getYesterday()) + '%')).all()
    try:
        # 同步到行为历史记录表 同时删除用户行为表的数据
        for behavior in behaviors:
            tmp = table_history_behavior_log(behavior.user_id)
            tmp.func_id = behavior.func_id
            tmp.begin_time = behavior.begin_time
            tmp.duration = behavior.duration
            db_session.add(tmp)
            db_session.delete(behavior)
        db_session.commit()
        print ("timingSyncData 同步数据成功")
    except Exception,e:
        print "timingSyncData - Exception:",e
    # behaviors = table_behavior_log.query.fileter().all()
    # print behaviors

def behavior_user(array):
    # "10002", dict['f'], dict['b'], dict['d']

    user = None
    try:
        # user = User.query.filter(User.user_id == user_id).first()
        user = User.query.filter(User.user_id == "10002").first()
        try:
            for dict in array:

                timeStamp = dict['b']
                # 秒转换为时间
                timeArray = time.localtime(timeStamp)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


                behavior = table_behavior_log(user.id)
                behavior.func_id = dict['f']
                behavior.begin_time = otherStyleTime
                behavior.duration = dict['d']
                db_session.add(behavior)

            db_session.commit()
            print ('提交成功')
        except Exception, e:
            print ("异常 插入用户行为异常", e)
    except Exception,e:
        print ("异常 查询 user_id 失败", e)

    print "here ~~~~~~~~~"


def register_user():
    #  user_id = ticks%10000*100000*1000+1*1000
    today = datetime.datetime.now()
    # 00000 000 000
    first = int(time.time()) / 1000000 % 1000
    second = int(time.time()) / 1000 % 1000
    third = int(time.time()) % 1000
    times = first * 10000000 + second * 10000 + third * 10 - 3950000000 + int(random.uniform(0, 9))
    print "second", time.time(), id, times, 'first:', first, 'second', second, 'third', third

    # user_id为十位
    u = User(name="lucy", pwd="123456", user_id=str(times))
    u.uuid = ""
    u.device = ""

    # print 'uuid',uuid
    u.last_time = today
    try:
        db_session.add(u)
        db_session.commit()
        return u
    except Exception, e:
        print "用户名 重复", e
        return None