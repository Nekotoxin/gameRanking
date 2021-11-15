#文件名:db.py
#功能：数据库操作
#功能函数包括：初始化数据库，插入数据，查询数据，更新数据，删除数据，关闭数据库,按照评分排序
import click
from flask import current_app, g,session
from flask.cli import with_appcontext
import pymysql
#######################

HOSTNAME='localhost'
USERNAME='root'
PASSWORD='000000'
DATABASENAME='gamerank'

db=pymysql.connect(host=HOSTNAME,user=USERNAME,password=PASSWORD,db=DATABASENAME,charset='utf8')

def init_app(app):
    #app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def init_db():
    return 0

def register_user(username,password):
    return 0

def login_user(username,password):
    return 0

# def close_db():
#     return 0

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

