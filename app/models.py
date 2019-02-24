# coding: utf-8

__author__ = "lau.wenbo"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "mysql://root:123456@127.0.0.1/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(30), unique=True)
    # 个人简介
    info = db.Column(db.Text)
    # 头像
    face = db.Column(db.String(255), unique=True)
    # 加入时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    # uuid 唯一ID
    uuid = db.Column(db.String(255), unique=True)
    # userlog 关联,外键相互关联
    userlogs = db.relationship('Userlog',backref='user')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    # 会员ID
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # 登陆IP
    IP= db.Column(db.String(100))
    # 日志添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Userlog %r>" % self.id


