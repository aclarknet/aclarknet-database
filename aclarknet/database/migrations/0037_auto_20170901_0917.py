# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0036_auto_20170901_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimate',
            name='doc_id',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='doc_id',
        ),
    ]
