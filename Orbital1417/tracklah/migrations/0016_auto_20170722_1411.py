# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracklah', '0015_charityprojects_shortdescrip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charityprojects',
            name='shortDescrip',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]