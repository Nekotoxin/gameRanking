#文件名:db.py
#功能：数据库操作
#功能函数包括：初始化数据库，插入数据，查询数据，更新数据，删除数据，关闭数据库,按照评分排序
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()
def init_app(app):
    db = SQLAlchemy(app)


class game_info(db.Model):
    game_id=db.Column(db.Integer, primary_key=True)
    game_title=db.Column(db.String(80), unique=True, nullable=False)
    game_score=db.Column(db.Float)
    game_type=db.Column(db.String(30))
    game_intro=db.Column(db.String(400))
    game_graph_path=db.Column(db.String(100))#相对目录下文件名称，以^分割
    game_update_time=db.Column(db.DateTime)
    game_collect_num=db.Column(db.Integer)
    game_comments_num=db.Column(db.Integer)
class comments(db.Model):
    comments_id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_info.user_id'))
    comment_time=db.Column(db.DateTime)
    conment_contents=db.Column(db.String(400))

class userinfo(db.Model):
    user_id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(80), unique=True, nullable=False)
    user_regis_time=db.Column(db.DateTime)
    user_self_intro=db.Column(db.String(400))
    

