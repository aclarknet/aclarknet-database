# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_appsettings_icon_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(blank=True, null=True, verbose_name='Avatar URL'),
        ),
    ]
