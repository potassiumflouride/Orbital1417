# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import pairing.models


class Migration(migrations.Migration):

    dependencies = [
        ('pairing', '0002_auto_20170718_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairing',
            name='img',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=pairing.models.upload_location, width_field='width_field'),
        ),
    ]
