#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Person(User):

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    # natual_key的序列化
    def natural_key(self):
        return '%s %s' % (self.last_name, self.first_name)

    class Meta:
        proxy = True
        ordering = ('first_name', )


class CY(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'成语')
    spell = models.CharField(max_length=128, verbose_name=u'拼音')
    content = models.TextField(max_length=1024, verbose_name=u'释义')
    derivation = models.TextField(max_length=1024, blank=True, verbose_name=u'出处')
    samples = models.CharField(max_length=1024, blank=True, verbose_name=u'示例')
    first = models.CharField(max_length=24, blank=True, verbose_name=u'首字拼音')
    last = models.CharField(max_length=24, blank=True, verbose_name=u'尾字拼音')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u'成语'
        verbose_name_plural = u'成语'


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name=u'父级分类')
    name = models.CharField(max_length=12, verbose_name=u'分类')
    description = models.TextField(max_length=64, blank=True, verbose_name=u'描述')

    def __unicode__(self):
        return u'%s' % self.name

    # natual_key的序列化
    def natural_key(self):
        return self.name

    class Meta:
        verbose_name = u'文章分类'
        verbose_name_plural = u'文章分类'


class Article(models.Model):
    title = models.CharField(max_length=32, verbose_name=u'标题')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name=u'日期')
    auth = models.ForeignKey(Person, verbose_name=u'作者')
    content = RichTextField(verbose_name=u'正文')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = u'博文'
        verbose_name_plural = u'博文'


class Welcome(models.Model):
    welcome = RichTextField(verbose_name=u'欢迎语')
    shell = models.CharField(max_length=32, verbose_name=u'等待输入')
    title = models.CharField(max_length=32, verbose_name=u'网站标题', default=u'Shell Blog')

    def __unicode__(self):
        return u'%s' % self.shell

    class Meta:
        verbose_name = u'配置'
        verbose_name_plural = u'配置'


class Help(models.Model):
    name = models.CharField(max_length=12, verbose_name=u'命令名')
    description = models.CharField(max_length=128, verbose_name=u'说明')
    samples = models.CharField(max_length=128, verbose_name=u'例子', blank=True)
    order = models.IntegerField(verbose_name=u'顺序', )
    display = models.BooleanField(verbose_name=u'是否展示', default=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u'帮助'
        verbose_name_plural = u'命令说明'
        ordering = ['order']


