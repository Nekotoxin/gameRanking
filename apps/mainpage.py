#文件名：mainpage.py
#访问网址：http://127.0.0.1:5000/ 后的响应路由写在这里
#该网址为网站主页，目前功能为显示游戏排名
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .. import db_control
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
def mainpage(game_year=None):
    #创建字典变量，存储游戏信息
    #@hughdazz创建一个游戏字典game_list_order_by_score 按照游戏评分顺序排序

    if game_year is not None:
        return db_control.year_list(game_year)
    games=getalltest()
    return render_template('/mainpage/mainpage.html',games=games,current_user=current_user)


#collect
@MainPageBP.route('/collect')
def collect():
    if request.method == 'POST':
        # 获取游戏id
        game_id = request.form['game_id']
        if game_id:
        # 插入分数
            user_id=current_user.id
        # 向jquery返回"success"
            games=db_control.collect_list(user_id)
            if game_id in games:
                return "collectSuccess"
            else:
                return "cancelSuccess"
    return "fail"

@MainPageBP.route('/?game_year=<game_year>')
def select_by_year(game_year):
    return db_control.year_list(game_year)