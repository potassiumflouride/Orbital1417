# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracklah', '0008_auto_20170717_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charpost',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='charpost',
            name='image_2',
        ),
        migrations.AddField(
            model_name='charpost',
            name='img1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]