# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 23:24
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0042_auto_20170609_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='uuid',
            field=models.CharField(default=uuid.UUID('b1a33b87-6c4b-4186-b866-70af3f78a0a5'), max_length=300, verbose_name='UUID'),
        ),
    ]
