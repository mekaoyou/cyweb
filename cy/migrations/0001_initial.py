# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('spell', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=1024)),
                ('derivation', models.CharField(max_length=1024)),
                ('samples', models.CharField(max_length=1024)),
                ('first', models.CharField(max_length=24)),
                ('last', models.CharField(max_length=24)),
            ],
        ),
    ]
