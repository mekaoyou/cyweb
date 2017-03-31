# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 01:42
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='\u5206\u7c7b')),
                ('description', models.TextField(blank=True, max_length=64, verbose_name='\u63cf\u8ff0')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cy.Category')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5206\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
        ),
        migrations.AlterModelOptions(
            name='cy',
            options={'verbose_name': '\u6210\u8bed', 'verbose_name_plural': '\u6210\u8bed'},
        ),
        migrations.AlterField(
            model_name='cy',
            name='content',
            field=models.TextField(max_length=1024, verbose_name='\u91ca\u4e49'),
        ),
        migrations.AlterField(
            model_name='cy',
            name='derivation',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1024, verbose_name='\u51fa\u5904'),
        ),
        migrations.AlterField(
            model_name='cy',
            name='first',
            field=models.CharField(blank=True, max_length=24, verbose_name='\u9996\u5b57\u62fc\u97f3'),
        ),
        migrations.AlterField(
            model_name='cy',
            name='last',
            field=models.CharField(blank=True, max_length=24, verbose_name='\u5c3e\u5b57\u62fc\u97f3'),
        ),
        migrations.AlterField(
            model_name='cy',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u6210\u8bed'),
        ),
        migrations.AlterField(
            model_name='cy',
            name='samples',
            field=models.CharField(blank=True, max_length=1024, verbose_name='\u793a\u4f8b'),
        ),
        migrations.AlterField(
            model_name='cy',
            name='spell',
            field=models.CharField(max_length=128, verbose_name='\u62fc\u97f3'),
        ),
    ]
