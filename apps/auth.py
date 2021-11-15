#文件名：auth.py
#功能：用户认证
#访问：http://127.0.0.1:5000/auth/login，http://127.0.0.1:5000/auth/register 等与账户登录挂钩的网址 后的响应写在这里
#功能包括：用户登录，用户注册，用户退出，用户登录状态管理
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from ..apps import AuthBP

###############################################################################
#   登录页面
#   route: /login
#   请求方式:GET，POST
#   请求参数:无
#   登陆成功：返回主页 (/)
#   登录失败：返回登录页面 (/auth/login.html)
###############################################################################
@AuthBP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #获取用户名和密码
        user_name = request.form['user_name']
        password = request.form['password']
        #..............................................
    return 0

###############################################################################
#   注册
#   链接:/register
#   请求方式:GET，POST
#   请求参数:无
#   注册成功：返回主页 (/)
#   注册失败：返回注册页面 (/auth/register.html)
###############################################################################
@AuthBP.route('/register', methods=['GET', 'POST'])
def register():
    return 0

###############################################################################
#   退出
#   链接:/logout
#   请求参数:无
#   退出成功：返回主页 (/)
###############################################################################
@AuthBP.route('/logout')
def logout():
    return 0

#其余功能.................................................................







