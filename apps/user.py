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

@UserBP.route('/<user_name>/settings', methods=['GET', 'POST'])
def settings(user_name):
    if request.method == 'POST':
        newAvatar = request.files['NewAvatar']
        newUsername=request.form['newUsername']
        newPassword=request.form['newPassword']
        newDescription=request.form['newDescription']

        if newUsername != "":
            db_control.update_item_value(current_user.id,'user_info','user_name',newUsername)

        if newPassword != "":
            db_control.update_item_value(current_user.id,'user_info','user_password',generate_password_hash(newPassword))

        if newDescription != "":
            db_control.update_item_value(current_user.id,'user_info','user_self_intro',newDescription)


        if newAvatar.filename != '':

            basepath = os.path.dirname(__file__)
            nowpath='static\\userMaterialStock'+'\\'+str(current_user.id)
            if not os.path.exists(os.path.join(basepath, nowpath)):
                os.mkdir(os.path.join(basepath, nowpath))
            path=os.path.join(basepath, nowpath, 'avatar.jpg')
            if os.path.exists(path):
                os.remove(path)
            newAvatar.save(path)

    return render_template('user/settings.html',user_name=user_name)

#注销账户
@login_required
def cancel_user():
    message=db_control.delete_user(current_user.id)
    if (message == 'success'):
        flash('cancel success!')
    else:
        flash('failed')
    return redirect(url_for('mainpage'))


@UserBP.route('/submitNewGame', methods=['GET', 'POST'])
@login_required
def submit_new_game():
    if request.method == 'POST':
        game_title = request.form['game_title']
        game_description = request.form['game_description']
        game_type = request.form['game_type']
        game_company = request.form['game_company']
        game_cover = request.files['game_cover']
        #获取上传的多个截图文件 name="game_screenshots"
        game_screenshots = request.files.getlist('game_screenshots')

        id=db_control.query_game(game_title)
        if id is not None:
            flash('game already existed!')
            render_template('user/userhome.html')

        type=db_control.query_type(game_type)
        if type is None:
            type=db_control.add_type(game_type)

        id=db_control.add_game(type,game_title,game_description)

        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        if not os.path.exists(os.path.join(basepath, 'static\gameMaterialStock\\'+str(id))):
            os.mkdir(os.path.join(basepath, 'static\gameMaterialStock\\'+str(id)))
        game_cover.save(os.path.join(basepath, 'static\gameMaterialStock\\'+str(id),'game_cover.jpg'))
        #按照game_screenshot<i>.jpg的方式保存
        for i in range(len(game_screenshots)):
            game_screenshots[i].save(os.path.join(basepath, 'static\gameMaterialStock\\'+str(id),'game_screenshot'+str(i+1)+'.jpg'))
        flash('update success!')
    return render_template('user/newGame.html',current_user=current_user)

    # return redirect(url_for('user.user_home', user_name=current_user.user_name))

@UserBP.route('/<user_name>', methods=['GET', 'POST'])
def user_home(user_name):
    basepath = os.path.dirname(__file__)
    nowpath = 'static\\userMaterialStock' + '\\' + str(current_user.id)
    path=os.path.join(basepath,nowpath)

    #return render_template('user/userhome.html',current_user=current_user,userCollectGames=[],userComments=commits,GamesOfUserComments=[])#测试代码
    commits = db_control.get_item_value(current_user.id, 'user_info', 'comments')
    game=[]
    for games in commits:
        game.append(games.related_game)

    return render_template('user/userhome.html',
                           current_user=current_user,
                           userCollectGames=db_control.collect_list(current_user.id),
                           userComments=commits,
                           GamesOfUserComments=game,
                           userMaterialPath=path)