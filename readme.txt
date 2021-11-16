<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
网站主页参考：https://bangumi.tv/game/browser?sort=rank
分工：
@Nekotoxin：网站框架，前端
@royzhz：登录模块，用户主页后端
@hughdazz：网站主页后端，数据库部分
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

开发顺序:游戏排行榜(11.20前)->游戏详情(11.25前)->账户管理(11.30前)->发表评论(12.05前)

目前任务：网站主页(链接:http://127.0.0.1:5000/)
工作文件:
@hughdazz mainpage.py,db.py
@Nekotoxin mainpage.html,base.html



<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
命名规则:
class：以大写开头，大写分割单词         AaaBbbCcc
函数以及变量：全部小写，以下划线分割单词   aaa_bbb_ccc
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
数据库设计@hughdazz:
	数据库：
	数据库名字:gamerank
	表1：游戏表 表名：game_info (游戏资源文件存放在static/game...，这里只存游戏的id等，按照id索引资源路径)
	游戏表部分按照游戏的评分排序，游戏的评分越高，排序越靠前
	表2：游戏评论表 表名：comments
	（暂时想出这三个表）
	表3：用户表 表名：user_info


	gamerank
		gameinfo
			game_id,game_title,game_score,game_type,
			game_intro,game_graph_path,
			game_update_time,game_collect_num,
			game_comments_num,{comments_table_id}
		comments
			{user_id},comment_time,conment_contents,
		userinfo
			user_id,user_name,user_regis_time,user_self_intro,
			{collect_game_table,comment_table_id}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    




