# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0061_project_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
