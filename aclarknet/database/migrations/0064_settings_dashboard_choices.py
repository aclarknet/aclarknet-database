# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 19:21
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0063_auto_20170624_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='dashboard_choices',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('notes', 'Notes'), ('projects', 'Projects'), ('totals', 'Totals')], max_length=21, null=True),
        ),
    ]
