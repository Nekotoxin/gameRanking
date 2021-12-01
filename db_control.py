#文件名:db.py
#功能：数据库操作
#功能函数包括：初始化数据库，插入数据，查询数据，更新数据，删除数据，关闭数据库,按照评分排序
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,Blueprint
from datetime import datetime
import click
from __init__ import db
from werkzeug.security import check_password_hash
#对game_info,game_type,user_info,comment实现了add,delete,query,update接口
#生成测试数据库:cmd下 flask initdb --drop,flask forge

cmd = Blueprint('db', __name__) #created a Blueprint for this module



    
from models import game_info,game_type,user_info,comment

#插入一个game_info
#parm:type_id,,game_title,game_description
def add_game(type_id,game_title,game_description):
    gt=game_type.query.get(type_id)
    g=game_info(game_title=game_title,game_intro=game_description)
    gt.games.append(g)
    db.session.commit()
    return g.game_id

def getalltest():
    return game_info.query.all()

#查找一个game_info
#parm:title
#ret:game_info-list
def query_game(title):
    _g=game_info.query.filter_by(game_title=title).first()
    if(_g is None):
        return None
    return _g.game_id

#删除一个game_info
#parm:game_id
def delete_game(game_id):
    g=game_info.query.get(game_id)
    db.session.delete(g)
    db.session.commit()

#插入一个game_type,传入name(string)
def add_type(name=''):
    gt=game_type(type_name=name)
    db.session.add(gt)
    db.session.commit()
    return gt.type_id

#查找一个game_type
#parm:name
#ret:game_type-list
def query_type(name):
    gt=game_type.query.filter_by(type_name=name).first()
    if(gt is None):
        return None
    return gt.type_id

#删除一个game_type
#parm:type_id
def delete_type(type_id):
    gt=game_type.query.get(type_id)
    db.session.delete(gt)
    db.session.commit()

#插入一个user_info
#parm:name,intro
def add_user(name='',intro=''):
    u=user_info(user_name=name,user_self_intro=intro)
    db.session.add(u)
    db.session.commit()

#查找一个user_info
#parm:name
#ret:user_info-list
def query_user(name=''):
    u=user_info.query.filter_by(user_name=name).first()
    if(u is None):
        return None
    return u.id



#插入一个comment
#parm:game_id,id,contents
def add_comment(game_id,id,contents=''):
    c=comment(comment_contents=contents)
    g=game_info.query.get(game_id)
    u=user_info.query.get(id)
    g.comments.append(c)
    u.comments.append(c)
    db.session.commit()

#查找一个comment
#parm:game_id,id
#ret:comment(none:-1)
def query_comment(game_id,id):
    c=comment.query.filter_by(comment_game_id=game_id,comment_user_id=id).first()
    if(c is None):
        return None
    return c.comment_id

#删除一个comment
#parm:comment_id
def delete_user(comment_id):
    u=user_info.query.get(comment_id)
    db.session.delete(u)
    db.session.commit()

#再对查询到的数据更改后(add和delete操作不包括在内)，运行此函数保存更改
def update_all():
    db.session.commit()
#***************************************************************************************************
#*******************************新        需          求*********************************************
#***************************************************************************************************
def update_item_value(id,table_name,table_word,new_value):
    if(table_name=='game_info'):
        g=game_info.query.get(id)
        if(g is None):
            return 'fail'
        if(table_word=='game_title'):
            g.game_title=new_value
        if(table_word=='game_score'):
            g.game_score=new_value
        if(table_word=='game_intro'):
            g.game_intro=new_value
        if(table_word=='game_collect_num'):
            g.game_collect_num=new_value
        if(table_word=='game_comments_num'):
            g.game_comments_num=new_value
    
    if(table_name=='user_info'):
        u=user_info.query.get(id)
        if(u is None):
            return 'fail'
        if(table_word=='user_name'):
            u.user_name=new_value
        if(table_word=='user_email'):
            u.user_email=new_value
        if(table_word=='user_password'):
            u.user_password=new_value
        if(table_word=='user_self_intro'):
            u.user_self_intro=new_value
    
    if(table_name=='game_type'):
        gt=game_type.query.get(id)
        if(gt is None):
            return 'fail'
        if(table_word=='type_name'):
            gt.type_name=new_value
    
    if(table_name=='comment'):
        c=comment.query.get(id)
        if(c is None):
            return 'fail'
        if(table_word=='comment_contents'):
            c.comment_contents=new_value  
    
    db.session.commit()
    return 'success or no match'

def get_item_value(id,table_name,table_word):
    if(table_name=='game_info'):
        g=game_info.query.get(id)
        if(g is None):
            return 'fail'
        if(table_word=='game_title'):
            return g.game_title
        if(table_word=='game_score'):
            return g.game_score
        if(table_word=='game_intro'):
            return g.game_intro
        if(table_word=='game_collect_num'):
            return g.game_collect_num
        if(table_word=='game_comments_num'):
            return g.game_comments_num
        if(table_word=='game_update_time'):
            return g.game_update_time
    
    if(table_name=='user_info'):
        u=user_info.query.get(id)
        if(u is None):
            return 'fail'
        if(table_word=='user_name'):
            return u.user_name
        if(table_word=='user_email'):
            return u.user_email
        if(table_word=='user_password'):
            return u.user_password
        if(table_word=='user_regis_time'):
            return u.user_regis_time
        if(table_word=='user_self_intro'):
            return u.user_self_intro
    
    if(table_name=='game_type'):
        gt=game_type.query.get(id)
        if(gt is None):
            return 'fail'
        if(table_word=='type_name'):
            return gt.type_name
    
    if(table_name=='comment'):
        c=comment.query.get(id)
        if(c is None):
            return 'fail'
        if(table_word=='comment_contents'):
            return c.comment_contents  
    
    return 'no match'

def find_user(id):
    u=user_info.query.get(id)
    if(u is None):
        return 'fail'
    return u

#删除一个user_info
#parm:id
def delete_user(id):
    u=user_info.query.get(id)
    if(u is None):
        return 'fail'
    db.session.delete(u)
    db.session.commit()
    return 'success'

def check_username_password(name,passw):
    u=user_info.query.filter_by(user_name=name).first()
    if(u is None):
        return "cantfind"
    if(check_password_hash(u.user_password,passw)==False):
        return "passwordincorrect"
    print('yes')
    return u.id
    
def change_username(id,new_name):
    u=user_info.query.get(id)
    if(u is None):
        return "user no found!"
    un=user_info.query.filter_by(user_name=new_name).first()
    if(un is None):
        u.user_name=new_name
        return 'success'
    else:
        return 'fail'

def add_new_user(name,passw):
    i=user_info.query.filter_by(user_name=name).first()
    if(i is None):
        u=user_info(user_name=name,user_password=passw)
        db.session.add(u)
        db.session.commit()
        return u.id
    return 'name has existed'

#***************************************************************************************************

@cmd.cli.command('init-db')
def initdb():
    db.drop_all()
    db.create_all()
    print('***** Datebase created ****')

@cmd.cli.command('forge')
def forge():
    """Generate fake data."""
    games=[
    {'game_title':'塞尔达传说：荒野之息','game_scores':'5.0'},
    {'game_title':'ride horse','game_scores':'5.0'},
    {'game_title':'hello shit','game_scores':'5.0'},
    {'game_title':'fry cry','game_scores':'4.3'},
    {'game_title':'card set','game_scores':'2.0'},
    {'game_title':'big brother','game_scores':'3.3'}]
    
    t1=game_type(type_name='psp')
    t2=game_type(type_name='ns')
    t3=game_type(type_name='psv')

    g1=game_info(game_title=games[0]['game_title'],game_score=games[0]['game_scores'])
    g2=game_info(game_title=games[1]['game_title'],game_score=games[1]['game_scores'])
    g3=game_info(game_title=games[2]['game_title'],game_score=games[2]['game_scores'])
    g4=game_info(game_title=games[3]['game_title'],game_score=games[3]['game_scores'])
    g5=game_info(game_title=games[4]['game_title'],game_score=games[4]['game_scores'])

    u1=user_info(user_name='Jack',user_password='%&&^@*(@*)')
    u2=user_info(user_name='Hugh',user_password='@*&@)@)(@*')
    u3=user_info(user_name='Jane',user_password='__)!+@)_@++')

    c1=comment(comment_contents='very good')
    c2=comment(comment_contents='very bad')
    c3=comment(comment_contents='like shit')
    c4=comment(comment_contents='looks nice')

    u1.comments.append(c1)
    u1.comments.append(c2)
    u2.comments.append(c3)
    u3.comments.append(c4)

    g1.comments.append(c1)
    g2.comments.append(c2)
    g3.comments.append(c4)
    g4.comments.append(c3)

    t1.games.append(g1)
    t2.games.append(g2)
    t2.games.append(g4)
    t3.games.append(g3)
    t3.games.append(g5)


    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.commit()

    print('Done')
    
    

