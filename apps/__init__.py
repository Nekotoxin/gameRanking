from flask import Blueprint
#url_prefix：设置蓝图的URL前缀
AuthBP = Blueprint('auth', __name__, url_prefix='/auth',template_folder='templates')
GameBP = Blueprint('blog', __name__,url_prefix='/game',template_folder='templates')
HomeBp=Blueprint('home',__name__,url_prefix='/user',template_folder='templates')
MainPageBP=Blueprint('mainpage',__name__,template_folder='templates')