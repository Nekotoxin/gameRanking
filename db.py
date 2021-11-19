#文件名:db.py
#功能：数据库操作
#功能函数包括：初始化数据库，插入数据，查询数据，更新数据，删除数据，关闭数据库,按照评分排序
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db=SQLAlchemy()

class game_info(db.Model):
    game_id=db.Column(db.Integer, primary_key=True)
    game_title=db.Column(db.String(80), unique=True, nullable=False)
    game_score=db.Column(db.Float)
    # game_type=db.Column(db.String(30))
    #根据type查游戏
    game_type_id=db.Column(db.Integer, db.ForeignKey('game_type.type_id'),nullable=False)
    game_type=db.relationship('game_type',backref=db.backref('games', lazy=True))

    game_intro=db.Column(db.String(400))
    game_graph_path=db.Column(db.String(100))#相对目录下文件名称，以^分割
    game_update_time=db.Column(db.DateTime,default=datetime.utcnow)
    game_collect_num=db.Column(db.Integer)
    game_comments_num=db.Column(db.Integer)

    def __repr__(self):
        return '<game: %>' %self.game_title

class game_type(db.Model):
    type_id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(30))
    def __repr__(self):
        return '<type: %>' %self.type_name


class comment(db.Model):
    comment_id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_info.user_id'))
    game_id=db.Column(db.Integer,db.ForeignKey('game_info.game_id'))
    comment_time=db.Column(db.DateTime)
    conment_contents=db.Column(db.String(400))
    #一个评论和用户和游戏都有对应关系
    comments_game_id = db.Column(db.Integer, db.ForeignKey('game_info.game_id'),nullable=False)
    comments_game = db.relationship('game_info',backref=db.backref('comments', lazy=True))

    comments_user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'),nullable=False)
    comments_user = db.relationship('user_info',backref=db.backref('comments', lazy=True))

    def __repr__(self):
        return '<comments: %>' %self.conment_contents

class user_info(db.Model, UserMixin):
    user_id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(80), unique=True, nullable=False)
    user_regis_time=db.Column(db.DateTime)
    user_self_intro=db.Column(db.String(400))

    def __repr__(self):
        return '<user: %>' %self.user_name


    password_hash = db.Column(db.String(128))  # 储存密码


