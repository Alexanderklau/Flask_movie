# coding: utf-8
__author__ = "lau.wenbo"

from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views