# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0011_auto_20170401_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome',
            name='title',
            field=models.CharField(default='Shell Blog', max_length=32, verbose_name='\u7f51\u7ad9\u6807\u9898'),
        ),
    ]
