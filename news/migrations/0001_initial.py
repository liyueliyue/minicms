# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('slug', models.CharField(max_length=256, db_index=True, verbose_name='网址')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('publish', models.BooleanField(default=True, verbose_name='正式发布')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(null=True, auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(blank=True, verbose_name='作者', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '教程',
                'verbose_name': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='栏目名称')),
                ('slug', models.CharField(max_length=256, db_index=True, verbose_name='栏目网址')),
                ('intro', models.TextField(default='', verbose_name='栏目简介')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name='归属栏目'),
        ),
    ]
