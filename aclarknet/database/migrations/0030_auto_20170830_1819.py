# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0029_auto_20170829_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appsettings',
            old_name='exclude_hidden_notes',
            new_name='exclude_hidden',
        ),
    ]
