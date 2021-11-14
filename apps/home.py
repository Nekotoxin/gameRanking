#文件名：home.py
#功能：用户登录后的主页
#访问路径：http://127.0.0.1:5000/user/<user_name> 后的响应路由写在这里
import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from apps import HomeBP
