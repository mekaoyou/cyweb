#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class CY(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'成语')
    spell = models.CharField(max_length=128, verbose_name=u'拼音')
    content = models.TextField(max_length=1024, verbose_name=u'释义')
    derivation = RichTextField(max_length=1024, blank=True, verbose_name=u'出处')
    samples = models.CharField(max_length=1024, blank=True, verbose_name=u'示例')
    first = models.CharField(max_length=24, blank=True, verbose_name=u'首字拼音')
    last = models.CharField(max_length=24, blank=True, verbose_name=u'尾字拼音')

    def __unicode__(self):
        return u'%s' % self.name

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)

    class Meta:
        verbose_name = u'成语'
        verbose_name_plural = u'成语'
