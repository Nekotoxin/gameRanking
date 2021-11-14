from flask import Blueprint
AuthBP = Blueprint('auth', __name__, url_prefix='/auth',template_folder='templates')
GameBP = Blueprint('blog', __name__,template_folder='templates')
HomeBp=Blueprint('home',__name__,template_folder='templates')
MainPageBP=Blueprint('mainpage',__name__,template_folder='templates')