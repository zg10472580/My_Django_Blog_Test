# -*- coding: utf-8 -*-
# Time     :  2021/7/30 17:37
# Author   :  老飞机
# File     :  Cj_Sql.py
# Software :  PyCharm

import platform

osName = platform.system()
if (osName == 'Linux'):
    import pymysql as MySQLdb
else:
    import MySQLdb  #加载mysql数据库模块

'''
修改表某个字段的编码  varchar是字段类型
alter table 表名 change 字段名 字段名 varchar() character set utf8 not null;
例如
alter table table1 change name name varchar(36) character set utf8 not null;

修改表的编码
alter table 表名 default character set utf-8;
例如
alter table table1 default character set utf-8;

修改数据库的 编码
alter database 库名 default character set utf-8;
例如
alter database test default character set utf-8;

'''

conn = MySQLdb.connect(host="39.101.141.163", user="root",passwd="a04d687e2a0b807d",port=3306) #连接 MYSQL 数据库

cursor = conn.cursor()     #获取游标

cursor.execute("create database if not exists test")    #创建数据库‘blog’

cursor.execute("alter database test default character set utf8mb4")#修改库编码

cursor.execute("USE test")#选中库

cursor.execute("alter table blog_article change content content longtext character set utf8mb4 not null")#进入库修改字段的编码

cursor.execute("alter table blog_article default character set utf8mb4")#修改表的编码

conn.commit()  # 提交数据库

cursor.close() # 关闭游标

conn.close()   # 关闭连接