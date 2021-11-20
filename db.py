#文件名:db.py
#功能：数据库操作
#功能函数包括：初始化数据库，插入数据，查询数据，更新数据，删除数据，关闭数据库,按照评分排序
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,Blueprint
from datetime import datetime
from datetime import datetime
import click
#对game_info,game_type,user_info,comment实现了add,delete,query,update接口
#生成测试数据库:cmd下 flask initdb --drop,flask forge

cmd = Blueprint('db', __name__) #created a Blueprint for this module

db=SQLAlchemy()

def init_app(app):
    global db
    db = SQLAlchemy(app)
    
class game_info(db.Model):
    game_id=db.Column(db.Integer, primary_key=True)
    game_title=db.Column(db.String(80), unique=True, nullable=False)
    game_score=db.Column(db.Float)

    #根据type查游戏
    game_type_id=db.Column(db.Integer, db.ForeignKey('game_type.type_id'))
    comments = db.relationship('comment',backref=db.backref('related_game', lazy=True))

    game_intro=db.Column(db.String(400))

    game_update_time=db.Column(db.DateTime,default=datetime.utcnow)
    game_collect_num=db.Column(db.Integer)
    game_comments_num=db.Column(db.Integer)

    def __repr__(self):
        return '<game: %r>' % self.game_title

class game_type(db.Model):
    type_id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(30))
    #通过games字段查询属于当前type的所有game,game可通过type字段查询game_type
    games=db.relationship('game_info',backref=db.backref('type', lazy=True))

    def __repr__(self):
        return '<type: %r>' % self.type_name


class comment(db.Model):
    comment_id=db.Column(db.Integer, primary_key=True)
    comment_time=db.Column(db.DateTime,default=datetime.utcnow)
    comment_contents=db.Column(db.String(400))
    #一个评论和用户和游戏都有对应关系
    comment_game_id = db.Column(db.Integer, db.ForeignKey('game_info.game_id'))
    comment_user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'))

    def __repr__(self):
        return '<comment: %r>' %self.comment_contents

class user_info(db.Model):
    user_id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(80),nullable=False)
    user_regis_time=db.Column(db.DateTime,default=datetime.utcnow)
    user_self_intro=db.Column(db.String(400))

    comments = db.relationship('comment',backref=db.backref('related_user', lazy=True))

    def __repr__(self):
        return '<user: %r>' %self.user_name

#插入一个game_info
#parm:type_id,title,score,intro
def add_game(type_id,title='',score=0.0,intro='',):
    gt=game_type.query.get(type_id)
    g=game_info(game_title=title,game_score=score,game_intro=intro,game_collect_num=0,game_comments_num=0)
    gt.games.append(g)
    db.session.commit()

#查找一个game_info
#parm:title
#ret:game_info-list
def query_game(title):
    g=game_info.query.filter_by(game_title=title).all()
    return g

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

#查找一个game_type
#parm:name
#ret:game_type-list
def query_type(name):
    gt=game_type.query.filter_by(type_name=name).all()
    return gt

#删除一个game_type
#parm:type_id
def delete_game(type_id):
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
def query_user(name):
    u=user_info.query.filter_by(user_name=name).all()
    return u

#删除一个user_info
#parm:user_id
def delete_user(user_id):
    u=user_info.query.get(user_id)
    db.session.delete(u)
    db.session.commit()

#插入一个comment
#parm:game_id,user_id,contents
def add_comment(game_id,user_id,contents=''):
    c=comment(comment_contents=contents)
    g=game_info.query.get(game_id)
    u=user_info.query.get(user_id)
    g.comments.append(c)
    u.comments.append(c)
    db.session.commit()

#查找一个comment
#parm:game_id,user_id
#ret:comment(none:-1)
def query_comment(game_id,user_id):
    c=comment.query.filter_by(comment_game_id=game_id,comment_user_id=user_id).first()
    if(c is None):
        return -1
    return c

#删除一个comment
#parm:comment_id
def delete_user(comment_id):
    u=user_info.query.get(comment_id)
    db.session.delete(u)
    db.session.commit()

#再对查询到的数据更改后(add和delete操作不包括在内)，运行此函数保存更改
def update_all():
    db.session.commit()

@cmd.cli.command('init-db')
def initdb():
    db.drop_all()
    db.create_all()
    print('***** Datebase created ****')

@cmd.cli.command('forge')
def forge():
    """Generate fake data."""
    db.create_all()
    games=[{'game_title':'ride horse','game_scores':'5.0'},
    {'game_title':'hello shit','game_scores':'5.0'},
    {'game_title':'fry cry','game_scores':'4.3'},
    {'game_title':'card set','game_scores':'2.0'},
    {'game_title':'big brother','game_scores':'3.3'},
    {'game_title':'guess what','game_scores':'5.0'}]
    
    t1=game_type(type_name='psp')
    t2=game_type(type_name='ns')
    t3=game_type(type_name='psv')

    g1=game_info(game_title=games[0]['game_title'],game_score=games[0]['game_scores'])
    g2=game_info(game_title=games[1]['game_title'],game_score=games[1]['game_scores'])
    g3=game_info(game_title=games[2]['game_title'],game_score=games[2]['game_scores'])
    g4=game_info(game_title=games[3]['game_title'],game_score=games[3]['game_scores'])
    g5=game_info(game_title=games[4]['game_title'],game_score=games[4]['game_scores'])

    u1=user_info(user_name='Jack')
    u2=user_info(user_name='Hugh')
    u3=user_info(user_name='Jane')

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
    
    

