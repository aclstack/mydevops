# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.
class UserIPInfo(models.Model):
    ip = models.CharField(max_length=40, default='', verbose_name='ip地址')
    time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "用户访问地址信息表"
        verbose_name_plural = verbose_name
        db_table = "useripinfo"     # 定义表名称，不然默认为应用名 + 模型名


class BrowseInfo(models.Model):
    useragent = models.CharField(max_length=100, default='', verbose_name='用户浏览器agent', null=True)
    models.CharField(max_length=256, verbose_name='唯一设备ID', default='')
    userip = models.ForeignKey('UserIPInfo', on_delete=models.CASCADE)  # 定义外键 在Django 2.0 on_delete为必有参数

    class Meta:
        verbose_name = "用户浏览器信息表"
        verbose_name_plural = verbose_name
        db_table = "browseinfo"
