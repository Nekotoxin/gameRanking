import functools
import pymysql
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import hashlib
from apps import MainPageBP

###############################################################################
#   主页
#   route: /
#   