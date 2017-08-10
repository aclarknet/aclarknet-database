# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20170803_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsettings',
            name='show_hidden_notes',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(blank=True, choices=[('danger', 'Danger'), ('faded', 'Faded'), ('info', 'Info'), ('inverse', 'Inverse'), ('primary', 'Primary'), ('success', 'Success'), ('warning', 'Warning')], max_length=7, null=True),
        ),
    ]
