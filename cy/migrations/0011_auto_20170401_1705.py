# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0010_remove_help_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='display',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u5c55\u793a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='help',
            name='order',
            field=models.IntegerField(default=1, verbose_name='\u987a\u5e8f'),
            preserve_default=False,
        ),
    ]
