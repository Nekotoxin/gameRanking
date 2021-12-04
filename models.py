from __init__ import db
from datetime import datetime
from flask_login import UserMixin
collections = db.Table('collections',
    db.Column('user_id', db.Integer, db.ForeignKey('user_info.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('game_info.game_id'), primary_key=True),
)
experiences = db.Table('experiences',
    db.Column('exper_user_id', db.Integer, db.ForeignKey('user_info.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game_info.game_id')),
)
class game_info(db.Model):
    game_id=db.Column(db.Integer, primary_key=True)
    game_title=db.Column(db.String(80),nullable=False)

    #根据type查游戏
    game_type_id=db.Column(db.Integer, db.ForeignKey('game_type.type_id'))
    comments = db.relationship('comment',backref=db.backref('related_game', lazy=True))
    game_scores = db.relationship('game_score',backref=db.backref('related_game', lazy=True))
    game_intro=db.Column(db.String(1000))

    game_update_time=db.Column(db.DateTime,default=datetime.utcnow)
    game_collect_num=db.Column(db.Integer)
    game_comments_num=db.Column(db.Integer)

    def __repr__(self):
        return '<game: %r>' % self.game_title
class game_score(db.Model):
    score_id=db.Column(db.Integer, primary_key=True)
    score_value=db.Column(db.Integer)
    score_game_id=db.Column(db.Integer, db.ForeignKey('game_info.game_id'))

class game_type(db.Model):
    type_id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(30))
    #通过games字段查询属于当前type的所有game,game可通过type字段查询game_type
    games=db.relationship('game_info',backref=db.backref('type', lazy=True))
    def __repr__(self):
        return '<type: %r>' % self.type_name


class comment(db.Model):
    comment_id=db.Column(db.Integer, primary_key=True)
    comment_title=db.Column(db.String(80))
    comment_time=db.Column(db.DateTime,default=datetime.utcnow)
    comment_contents=db.Column(db.String(400))
    #一个评论和用户和游戏都有对应关系
    comment_game_id = db.Column(db.Integer, db.ForeignKey('game_info.game_id'))
    comment_user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    def __repr__(self):
        return '<comment: %r>' %self.comment_contents

class user_info(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(80),nullable=False)
    user_email=db.Column(db.String(80),unique=True)
    user_password=db.Column(db.String(256),nullable=False)
    user_regis_time=db.Column(db.DateTime,default=datetime.utcnow)
    user_self_intro=db.Column(db.String(400))

    comments = db.relationship('comment',backref=db.backref('related_user', lazy=True))
    collects = db.relationship('game_info', secondary=collections,backref=db.backref('related_collect_users', lazy='dynamic'))
    expers = db.relationship('game_info', secondary=experiences,backref=db.backref('related_exper_users', lazy='dynamic'))
    def __repr__(self):
        return '<user: %r>' %self.user_name