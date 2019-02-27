# coding: utf-8

__author__ = "lau.wenbo"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:123456@127.0.0.1/movie'
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
    userlogs = db.relationship('Userlog', backref='user')
    # 评论表关联
    comments = db.relationship('Comment', backref="user")
    moviecols = db.relationship('Moviecol', backref="user")


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


#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    movies = db.relationship("Movie", backref="tag")  #电影外键关系关联

    def __repr__(self):
        return "<Tag %r>" %self.name



#movie
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # 地址
    url = db.Column(db.String(255), unique=True)
    # 简介
    info = db.Column(db.Text)
    # 封面
    logo = db.Column(db.String(255), unique=True)
    # 星级
    star = db.Column(db.SmallInteger)
    # 播放量
    playnum = db.Column(db.BigInteger)
    # 评论量
    commentnum = db.Column(db.BigInteger)
    # 所属标签
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    # 上映地区
    area = db.Column(db.String(255))
    # 上映时间
    relese_time = db.Column(db.Date)
    # 播放时间
    length = db.Column(db.String(100))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    # 评论关联外键
    comments = db.relationship('Comment', backref="movie")
    # 收藏关联外键
    moviecols = db.relationship('Moviecol', backref="movie")



    def __repr__(self):
        return "<Movie %r>" % self.title

# 上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # 封面
    logo = db.Column(db.String(255), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Preview %r>" % self.title

# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    # 指向电影
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # 指向用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Comment %r>" % self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)
    # 指向电影
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # 指向用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    # 角色
    auths = db.Column(db.String(600))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Auth %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(30))
    # 是否为超级管理员
    is_super = db.Column(db.SmallInteger)
    # role_id, 所属角色
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    adminlog = db.relationship("adminlog", backref="admin")  #管理员登陆日志外键关系关联
    oplog = db.relationship("oplog", backref="admin")  #操作日志外键关系关联

    def __repr__(self):
        return "<admin %r>" % self.id


# 管理员登陆日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)
    # 会员ID
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # 登陆IP
    IP = db.Column(db.String(100))
    # 日志添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<adminlog %r>" % self.id

# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)
    # 会员ID
    admin_Id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # 登陆IP
    IP = db.Column(db.String(100))
    # 操作原因
    reason = db.Column(db.String(600))
    # 日志添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<oplog %r>" % self.id

if __name__ == "__main__":
    pass
    # db.create_all()