#后端连接方式； 代码链接
# from flask import Flask,jsonify #确保你导入是jsonify,jsonify 函数作用: 把python字典 转换为JSON字符串 
#更重要的是: 他会设置一个HTTP响应头 Content - type: application/json 告诉浏览器 我给你的是json数据 不是html网页

import connexion
from connexion import FlaskApp
from flask_sqlalchemy import SQLAlchemy #导入翻译官
from flask_marshmallow import Marshmallow #导入自动翻译机

import os #处理文件路径

basedir = os.path.abspath(os.path.dirname(__file__)) # os.path.dirname(__file__)指的是app.py所在的那个文件夹

#创建一个connexion应用，它内部封装了flask,自动读取swagger.yml合同
connexion_app = FlaskApp(__name__,specification_dir=basedir) 

flask_app = connexion_app.app

@flask_app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Max-Age'] = '86400'
    return response

#数据库配置: 告诉翻译官 你的文件叫 "contacts.db"
db_path = os.path.join(basedir,"contacts.db") #在根目录下然后创建一个名字叫contacts.db的文件嗷
flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path #告诉sqlite数据库 文件就是刚刚那个contacts.db
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #这是一个烦人的性能警告 让控制台保持干净

db = SQLAlchemy(flask_app) #把dp和app绑定了
ma = Marshmallow(flask_app) 

#定义数据模板 这个模板在python 名字叫Contact 
#（db.Model) 告诉翻译官这个类别

class Contact(db.Model):
    __tablename__ = 'contact' #这张表的名字叫contact

    #id 列: 是个整数 他是主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) #不允许为空
    phone = db.Column(db.String(120), nullable=False, unique=True) #是唯一的

connexion_app.add_api("swagger.yml")

with flask_app.app_context():
    db.create_all()


# #确保服务器可以被访问，并开启调试模式
# if __name__ == "__main__": #只有app.py直接被运行时才执行这些代码:
#     connexion_app.run(host="0.0.0.0", port=8000, reload=True)  #这一行是启动开发服务器的命令。
#     # 0.0.0.0 特殊的IP: 监听本机所有网络接口  8000 端口 相当于服务器IP的房间号  debug 一半设true哈