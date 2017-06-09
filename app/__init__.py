# -*- coding: utf-8 -*-
from flask import Flask
from app.config import init_db
from app.config import db_session

app = Flask(__name__)

from views import view
@app.route('/')
def hello_world():
    init_db()
    return 'Hello World!'



# 在您的应用当中以一个显式调用 SQLAlchemy , 您只需要将如下代码放置在您应用的模块中。
# Flask 将会在请求结束时自动移除数据库会话:
# @app.teardown_request
# def shutdown_session(exception=None):
#     db_session.remove()