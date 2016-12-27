# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-27 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='版块名称')),
                ('desc', models.CharField(max_length=100, verbose_name='版块描述')),
                ('manager_name', models.CharField(max_length=100, verbose_name='管理员名称')),
            ],
        ),
    ]
