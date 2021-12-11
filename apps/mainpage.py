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
def mainpage():
    #创建字典变量，存储游戏信息
    #@hughdazz创建一个游戏字典game_list_order_by_score 按照游戏评分顺序排序
    games=getalltest()
    return render_template('/mainpage/mainpage.html',games=games,current_user=current_user)


@MainPageBP.route('/<game_year>')
def mainpage_year(game_year):
    # if game_year=='favicon.ico':
    #     return "error"
    games=db_control.year_list(int(game_year))
    return render_template('/mainpage/mainpage.html', games=games, current_user=current_user)

#collect
@MainPageBP.route('/collect', methods=['GET', 'POST'])
def collect():
    if request.method == 'POST':
        # 获取游戏id
        game_id = request.form['game_id']
        if game_id:
            user_id=current_user.id

            if db_control.is_collect(user_id,game_id) == True:
                db_control.incollect_game(user_id, game_id)
                return "cancelSuccess"
            else:
                db_control.collect_game(user_id, game_id)
                return "collectSuccess"

    return "fail"
