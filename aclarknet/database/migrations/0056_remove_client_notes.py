# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 11:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0055_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='notes',
        ),
    ]