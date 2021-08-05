# Generated by Django 3.2.5 on 2021-08-04 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('source_id', models.CharField(max_length=25, verbose_name='文章id或source名称')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('user_name', models.CharField(max_length=25, verbose_name='评论用户')),
                ('url', models.CharField(max_length=100, verbose_name='链接')),
                ('comment', models.CharField(max_length=500, verbose_name='评论内容')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='UserSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('mailbox', models.CharField(max_length=30, verbose_name='邮箱')),
                ('date_time', models.DateField(auto_now_add=True, verbose_name='注册时间')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='博客标题')),
                ('date_time', models.DateField(auto_now_add=True, verbose_name='发表日期')),
                ('content', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('digest', models.TextField(blank=True, null=True, verbose_name='文章摘要')),
                ('view', models.BigIntegerField(default=0, verbose_name='阅读数')),
                ('comment', models.BigIntegerField(default=0, verbose_name='评论数')),
                ('picture', models.CharField(max_length=200, verbose_name='标题图片地址')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='分类')),
                ('tag', models.ManyToManyField(to='blog.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
                'ordering': ['-date_time'],
            },
        ),
    ]
