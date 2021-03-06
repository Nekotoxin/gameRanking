#文件名：game.py
#功能：在排行榜中点击进入某个游戏后展示的页面
#访问路径：http://127.0.0.1:5000/game/<game_id>后的响应route函数写在这里
import functools
import pymysql
import sys
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify
)
from flask_login import (login_required,current_user)
import hashlib
from . import GameBP
from db_control import *


@GameBP.route('/<game_id>',methods=['GET','POST'])
def gamepage(game_id):
    game = find_game_by_id(game_id)
    #获取当前相对路径
    path = os.path.dirname(os.path.abspath(__file__))
    #获取当前路径下的static文件夹下的gameMaterialStock文件夹下的<game_id>文件夹
    game_path = os.path.join(path, 'static', 'gameMaterialStock', game_id)
    # print(game_path)
    #获取当前路径下的static文件夹下的gameMaterialStock文件夹下的<game_id>文件夹下的所有文件个数
    game_file_num = len(os.listdir(game_path))
    #获取当前路径下的static文件夹下的gameMaterialStock文件夹下的<game_id>文件夹下的screenshot<i>.jpg 文件
    screenShotCount = 0
    for i in range(1, game_file_num+1):
        file_path = os.path.join(game_path, 'screenshot'+str(i)+'.png')
        #判断文件是否存在
        if os.path.exists(file_path):
            screenShotCount += 1
    
    #获取评论
    comments=query_comment_by_game_id(game_id)
    users=getalluser()
    print(game.game_average_score)
    print('*')
   
    # print(comments)
    return render_template('game/gamepage.html', game=game, screenShotCount=screenShotCount,comments=comments,current_user=current_user,users=users)

#submitScore
@GameBP.route('/submitScore',methods=['GET','POST'])
def submitScore():
    if request.method == 'POST':
        #获取游戏id
        game_id = request.form['game_id']
        #获取分数
        score = request.form['score']
        if game_id and score:
            #插入分数
            add_score(game_id,score)
            #向jquery返回"success"
            game=find_game_by_id(game_id)
            print(game.game_average_score)
            print('&')
            print('add score success')
            return "success"

#addComment
@GameBP.route('/submitComment',methods=['GET','POST'])
def submitComment():
    if current_user.is_authenticated is False:
        return redirect(url_for("auth.login"),code=302)
    if request.method == 'POST':
        #获取用户id
        user_id = current_user.get_id()
        #获取游戏id
        game_id = request.form['game_id']
        #获取评论内容
        comment = request.form['comment_content']
        if game_id and comment:
            #插入评论
            add_comment(game_id,user_id,comment)
            return "success"
    return "fail"