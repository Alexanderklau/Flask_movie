# coding: utf-8

__author__ = "lau.wenbo"

from app.home import home

@home.route("/")
def index():
    return "<h1 sytle='color:red'>this is home</h1>"