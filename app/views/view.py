# -*- coding: utf-8 -*-
import json

from flask import request, jsonify

from app import app
from app.mysql import query

@app.route('/a2',methods=['GET'])
def a2():
    query.test()
    return jsonify({"a":"b"})

@app.route('/a3',methods=['GET'])
def a3():
    query.test01()
    return jsonify({"a":"b"})




@app.route('/a1',methods=['POST'])
def a1():
    user_id = request.form.get("u")
    func_id = request.form.get("func_id")
    begin_time = request.form.get("begin_time")
    duration = request.form.get("duration")

    value = request.form.get('value')
    json_dict =  json.loads(value)

    # print ('json_dict',json_dict["bb"][5]["b"])
    # print (value)

    if json_dict.has_key('bb'):
        query.behavior_user(json_dict["bb"])

        return jsonify({"aa":"dd"})
    else:
        print ('不是字典')

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

# 实例化BackgroundSchedule对象
scheduler = BackgroundScheduler()
scheduler.start()

def loginusersAtOneDay():
    query.timingSyncData()
    print "定时同步用户行为数据成功"

scheduler.add_job(
    func=loginusersAtOneDay,
    trigger='cron',
    month = '1-12',
    hour = '11',
    minute = '41'
)


atexit.register(lambda:scheduler.shutdown())