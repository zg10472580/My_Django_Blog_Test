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

conn = MySQLdb.connect(host="39.1141.163", user="root",passwd="xxx",port=3306) #连接 MYSQL 数据库

cursor = conn.cursor()     #获取游标

cursor.execute("create database if not exists 你的数据库")    #创建数据库 ‘ 你的数据库 ’

cursor.execute("alter database 你的数据库 default character set utf8mb4")#修改库编码

cursor.execute("USE 你的数据库")#选中库

cursor.execute("alter table 你要修改的表 change content content longtext character set utf8mb4 not null")#进入库修改字段的编码

cursor.execute("alter table 你要修改的表 default character set utf8mb4")#修改表的编码

conn.commit()  # 提交数据库

cursor.close() # 关闭游标

conn.close()   # 关闭连接
