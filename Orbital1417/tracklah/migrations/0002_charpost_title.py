# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracklah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charpost',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
