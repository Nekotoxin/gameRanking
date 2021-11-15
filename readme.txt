网站主页参考：https://bangumi.tv/game/browser?sort=rank
分工：
@Nekotoxin：网站框架，前端
@royzhz：登录模块，用户主页后端
朱：网站主页后端，数据库部分

数据库：
数据库名字:gamerank
表1：游戏表 表名：game (游戏资源文件存放在static/game...，这里只存游戏的id等，按照id索引资源路径)
游戏表部分按照游戏的评分排序，游戏的评分越高，排序越靠前
表2：游戏评论表 表名：comment
（暂时想出这三个表）
表3：用户表 表名：user


开发顺序:游戏排行榜(11.20前)->游戏详情(11.25前)->账户管理(11.30前)->发表评论(12.05前)

目前任务：网站主页(链接:http://127.0.0.1:5000/)
工作文件:
@朱 mainpage.py,db.py 
@Nekotoxin mainpage.html,base.html

数据库创建表:game
    前端需求：传过来一个字典，名为games    
    形式：@return render_template('/mainpage.html', games=games)
    1.游戏表成员：游戏名称，游戏id，游戏评分，游戏类型，游戏简介，游戏图片路径，游戏更新时间，游戏收藏数，游戏评论数
    2.按id遍历游戏表，评分为从高到低

    前端使用games字典的方法，示例：
        {% for game in games %}
        索引详细项方法：game['name']
                game['points']等
        {% endfor %}
    
    




