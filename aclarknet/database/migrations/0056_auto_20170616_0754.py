# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0055_auto_20170615_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='parties',
        ),
        migrations.RemoveField(
            model_name='contractsettings',
            name='parties',
        ),
    ]
