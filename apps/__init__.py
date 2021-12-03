from flask import Blueprint
#url_prefix：设置蓝图的URL前缀
AuthBP = Blueprint('auth', __name__, url_prefix='/auth',template_folder='templates')
GameBP = Blueprint('game', __name__,url_prefix='/game',template_folder='templates')
UserBP=Blueprint('user',__name__,url_prefix='/user',template_folder='templates')
MainPageBP=Blueprint('mainpage',__name__,template_folder='templates')