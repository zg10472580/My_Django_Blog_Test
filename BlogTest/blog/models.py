# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from mdeditor.fields import MDTextField


# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField('标签名称', max_length=30)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name="博客标题")  # 博客标题
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE)
    #DateField  创建时间段
    date_time = models.DateField(auto_now_add=True,verbose_name="发表日期")  # 博客日期
    # content = models.TextField(blank=True, null=True,verbose_name="正文")  # 文章正文
    content = MDTextField('正文')
    #TextField    字符串=longtext ，一个容量很大的文本字段， admin 管理界面用 <textarea>多行编辑框表示该字段数据。
    digest = models.TextField(blank=True, null=True,verbose_name="文章摘要")  # 文章摘要
    #在user表设置author为主键
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    #BigIntegerField  长整形
    view = models.BigIntegerField(default=0,verbose_name="阅读数")  # 阅读数
    #BigIntegerField  长整形
    comment = models.BigIntegerField(default=0,verbose_name="评论数")  # 评论数
    #CharField  字符串字段
    picture = models.CharField(max_length=200,verbose_name="标题图片地址")  # 标题图片地址
    #ManyToManyField  创建多字段数据
    tag = models.ManyToManyField(Tag,verbose_name="标签")  # 标签

    def __str__(self):
        return self.title

    def sourceUrl(self):
        source_url = settings.HOST + '/blog/detail/{id}'.format(id=self.pk)
        return source_url  # 给网易云跟帖使用

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']
        verbose_name = "文章管理"
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField('分类', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "文章类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField("标题", max_length=100)
    source_id = models.CharField('文章id或source名称', max_length=25)
    create_time = models.DateTimeField('评论时间', auto_now=True)
    user_name = models.CharField('评论用户', max_length=25)
    url = models.CharField('链接', max_length=100)
    comment = models.CharField('评论内容', max_length=500)

class UserSheet(models.Model):
    username = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=30)
    mailbox = models.CharField('邮箱', max_length=30)
    # DateField  创建时间段
    date_time = models.DateField(auto_now_add=True, verbose_name="注册时间")  # 博客日期

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "网站的用户"
        verbose_name_plural = verbose_name