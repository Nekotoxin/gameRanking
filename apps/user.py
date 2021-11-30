#文件名：home.py
#访问网址：http://127.0.0.1:5000/user/<user_name> 后的响应路由写在这里
#该网址显示用户信息，包括修改密码，修改用户名，更换头像，注销用户等
import functools
import os
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


@UserBP.route('/<user_name>/userhome', methods=['GET', 'POST'])
@login_required
def submit_new_game():
    if request.method == 'POST':
        game_title = request.form['game_title']
        game_description = request.form['game_description']
        game_type = request.form['game_type']
        game_company = request.form['game_company']
        game_cover = request.files['game_cover']
        game_screenshot1= request.files['game_screenshot1']
        game_screenshot2 = request.files['game_screenshot2']
        game_screenshot3 = request.files['game_screenshot3']
        game_screenshot4 = request.files['game_screenshot4']
        game_screenshot5 = request.files['game_screenshot5']

        id=db_control.query_game(game_title)
        if id is not None:
            flash('game already existed!')
            render_template('user/userhome.html')

        type=db_control.query_type(game_type)
        if type is None:
            type=db_control.add_type(game_type)

        db_control.add_game(type,game_title,game_description)

        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        game_cover.save(os.path.join(basepath, 'static\gameMaterialStock\id','game_cover'))
        game_screenshot1.save(os.path.join(basepath, 'static\gameMaterialStock\id','game_screenshot1'))
        game_screenshot2.save(os.path.join(basepath, 'static\gameMaterialStock\id','game_screenshot2'))
        game_screenshot3.save(os.path.join(basepath, 'static\gameMaterialStock\id','game_screenshot3'))
        game_screenshot4.save(os.path.join(basepath, 'static\gameMaterialStock\id','game_screenshot4'))
        game_screenshot5.save(os.path.join(basepath, 'static\gameMaterialStock\id','game_screenshot5'))
        flash('update success!')
        return render_template('user/userhome.hyml')
    return render_template('user/userhome.hyml')