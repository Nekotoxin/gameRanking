#文件名：home.py
#访问网址：http://127.0.0.1:5000/user/<user_name> 后的响应路由写在这里
#该网址显示用户信息，包括修改密码，修改用户名，更换头像，注销用户等
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_login import (login_required,current_user)
from werkzeug.security import generate_password_hash, check_password_hash
from ..apps import UserBP
from .. import db_control
import pymysql
@UserBP.route('/<user_name>', methods=['GET', 'POST'])
@login_required
def user(user_name):
    return 'hello user_name:'+user_name



@login_required
def reset_name():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return render_template('user/settings.html')

        message=db_control.change_username(current_user.id, name)
        if(message=='success'):
            flash('userid has changed')
        else:
            flash('failed')
        return redirect(url_for('mainpage'))#调用主页函数，需要修改
    return render_template('user/settings.html')


#传入老密码，正确后进入下一步
@login_required
def reset_password():
    if request.method == 'POST':
        old_password = request.form['old_password']
        if (check_password_hash(current_user.password,old_password)==0):
            flash('password incorrect!')
            render_template('user/settings.html')


        new_password = request.form['new_password']
        new_password=generate_password_hash(new_password)

        message=db_control.change_user_password(current_user.id,new_password)
        if(message=='success'):
            flash('password has changed')
            return render_template('/auth/login.html')
        else:
            flash('failed')
            return render_template('user/settings.html')

    return render_template('user/settings.html')

#注销账户
@login_required
def cancel_user():
    message=db_control.delete_user(current_user.id)
    if (message == 'success'):
        flash('cancel success!')
    else:
        flash('failed')
    return redirect(url_for('mainpage'))


