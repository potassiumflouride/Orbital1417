# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_auto_20170617_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
