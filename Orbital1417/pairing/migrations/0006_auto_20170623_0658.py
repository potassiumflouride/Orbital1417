# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pairing', '0005_auto_20170622_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pairingsignupdata',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='pairingsignupdata',
            name='contact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pairingsignupdata',
            name='experiences',
            field=models.CharField(max_length=20),
        ),
    ]