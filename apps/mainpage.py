#文件名：mainpage.py
#访问网址：http://127.0.0.1:5000/ 后的响应路由写在这里
#该网址为网站主页，目前功能为显示游戏排名
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from ..apps import MainPageBP
###############################################################################
#   主页
#   route: /
###############################################################################
@MainPageBP.route('/')
def mainpage():
    #创建字典变量，存储游戏信息
    return 'hello world'