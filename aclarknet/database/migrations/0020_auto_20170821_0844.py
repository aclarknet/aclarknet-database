# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_auto_20170821_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Rate (United States Dollar - USD)'),
        ),
    ]
