#文件名：auth.py
#功能：用户认证
#访问：http://127.0.0.1:5000/auth/login，http://127.0.0.1:5000/auth/register 等与账户登录挂钩的网址 后的响应写在这里
#功能包括：用户登录，用户注册，用户退出，用户登录状态管理
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_login import (LoginManager,login_user,logout_user,login_required)
from werkzeug.security import generate_password_hash, check_password_hash
from ..apps import AuthBP
from .. import db_control




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
        user_name = request.form['username']
        password = request.form['password']

        if not user_name or not password:
            flash('Invalid input')
            return redirect(url_for('login'))

        password=generate_password_hash(password)
        user=db_control.check_username_password(user_name,password)

        if(user == 'cantfind'):
            flash('Invalid username')
            return render_template('/auth/login.html')
        elif(user=='passwordincorrect'):
            flash('password incorrect!')
            return render_template('/auth/login.html')#需要修改到主页函数
        else:
            login_user(user)
            flash('login success')
            return render_template('/auth/login.html')

    return render_template('/auth/login.html')

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
    if request.method=='POST':
        user_name = request.form['name']
        password = request.form['password']

        password = generate_password_hash(password)
        user = db_control.check_username_password(user_name,password) # 获取用户信息

        if(user == 'cantfind'):#名字可用
            db_control.add_new_user(user_name,password)
            flash('register success!')
            return render_template('/auth/register.html')
        else:#名字不可用
            flash('the name has been registered!')
            return render_template('/auth/register.html')

    return render_template('/auth/register.html')

###############################################################################
#   退出
#   链接:/logout
#   请求参数:无
#   退出成功：返回主页 (/)
###############################################################################
@AuthBP.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout success!')
    return render_template('/auth/register.html')
#其余功能.................................................................