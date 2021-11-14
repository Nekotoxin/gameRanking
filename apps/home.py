#文件名：home.py
#访问网址：http://127.0.0.1:5000/user/<user_name> 后的响应路由写在这里
#该网址显示用户信息，包括修改密码，修改用户名，更换头像，注销用户等
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from apps import HomeBP
