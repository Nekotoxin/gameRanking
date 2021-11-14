#文件名：game.py
#功能：在排行榜中点击进入某个游戏后展示的页面
#访问路径：http://127.0.0.1:5000/game/<game_id>后的响应route函数写在这里
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from apps import GameBP

