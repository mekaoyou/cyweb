# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0012_auto_20170401_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='help',
            options={'ordering': ['order'], 'verbose_name': '\u5e2e\u52a9', 'verbose_name_plural': '\u547d\u4ee4\u8bf4\u660e'},
        ),
        migrations.AddField(
            model_name='help',
            name='samples',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u4f8b\u5b50'),
        ),
    ]
