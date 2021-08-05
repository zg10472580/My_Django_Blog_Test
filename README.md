

# 特点

* markdown 渲染，代码高亮
* 三方社会化评论系统支持(畅言)
* 背景随机切换
* 阅读排行榜/最新发表
* 多目标源博文分享
* 博文归档

### 为了测试 我的数据库是sqlite3  各位可以在 settings.py更改你们的mysql数据库

# 安装
```
pip install -r requirements.txt  # 安装所有依赖
修改setting.py配置数据库
配置畅言：到http://changyan.kuaizhan.com/注册站点,将blog/templates/blog/message.html中js部分换成你在畅言中生成的APP ID APP SECRET。
畅言js位置: 进入工作台-》通用设置-》填好 网站基本信息 》回到 》 后台总览 》复制APPID APPSECRET到message.html中
python manage.py makemigrations blog
python manage.py migrate
python manage.py runserver
```

### 示例博客：<http://39.101.141.163:889>
