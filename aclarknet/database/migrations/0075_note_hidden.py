# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-02 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0074_auto_20170701_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]