#文件名：game.py
#功能：在排行榜中点击进入某个游戏后展示的页面
#访问路径：http://127.0.0.1:5000/game/<game_id>后的响应route函数写在这里
import functools
import pymysql
import sys,os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from . import GameBP
from db_control import *


@GameBP.route('/<game_id>')
def gamepage(game_id):
    game=find_game_by_id(game_id)
    #获取当前相对路径
    path=os.path.dirname(os.path.abspath(__file__))
    #获取当前路径下的static文件夹下的gameMaterialStock文件夹下的<game_id>文件夹
    game_path=os.path.join(path,'static','gameMaterialStock',game_id)
    # print(game_path)
    #获取当前路径下的static文件夹下的gameMaterialStock文件夹下的<game_id>文件夹下的所有文件个数
    game_file_num=len(os.listdir(game_path))
    # print(game_file_num)
    #获取当前路径下的static文件夹下的gameMaterialStock文件夹下的<game_id>文件夹下的game_screenshot<i>.jpg 文件
    screenShotCount=0
    for i in range(1,game_file_num+1):
        file_path=os.path.join(game_path,'game_screenshot'+str(i)+'.jpg')
        #判断文件是否存在
        if os.path.exists(file_path):
            screenShotCount+=1
    print(screenShotCount)
    return render_template('game/gamepage.html',game=game,screenShotCount=screenShotCount)
