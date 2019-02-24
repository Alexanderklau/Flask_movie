# coding: utf-8

__author__ = "lau.wenbo"

from app.admin import admin

@admin.route("/")
def index():
    return "<h1 sytle='color:green'>this is admin</h1>"