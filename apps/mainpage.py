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
from flask_login import (login_required,current_user)
from ..db_control import (
    query_game,getalltest
)
###############################################################################
#   主页
#   route: /
###############################################################################
@MainPageBP.route('/')
def mainpage():
    #创建字典变量，存储游戏信息
    #@hughdazz创建一个游戏字典game_list_order_by_score 按照游戏评分顺序排序
    games=getalltest()
    return render_template('/mainpage/mainpage.html',games=games,current_user=current_user)
#collect
@MainPageBP.route('/collect')
def collect():
    return 0