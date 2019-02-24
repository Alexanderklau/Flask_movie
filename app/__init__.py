# coding: utf-8

__author__ = "lau.wenbo"

from flask import Flask

app = Flask(__name__)
app.debug - True

from app.home import home as home_blue
from app.admin import admin as admin_blue

app.register_blueprint(home_blue)
app.register_blueprint(admin_blue, url_prefix="/admin")

