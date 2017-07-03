# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import faker.providers.lorem.la


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0078_remove_company_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractsettings',
            name='authority_to_act',
            field=models.TextField(blank=True, null=True, verbose_name='Authority to Act'),
        ),
        migrations.AddField(
            model_name='contractsettings',
            name='contributor_assignment_agreement',
            field=models.TextField(blank=True, null=True, verbose_name='Contributor Assignment Agreement'),
        ),
        migrations.AddField(
            model_name='contractsettings',
            name='parties',
            field=models.TextField(blank=True, null=True, verbose_name='Parties'),
        ),
        migrations.AddField(
            model_name='contractsettings',
            name='payment_terms',
            field=models.TextField(blank=True, null=True, verbose_name='Payment Terms'),
        ),
        migrations.AddField(
            model_name='contractsettings',
            name='period_of_agreement',
            field=models.TextField(blank=True, null=True, verbose_name='Period of Agreement'),
        ),
        migrations.AddField(
            model_name='contractsettings',
            name='scope_of_work',
            field=models.TextField(blank=True, null=True, verbose_name='Scope of Work'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='complete_agreement',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Complete Agreement'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='confidentiality',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Confidentiality'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='governing_laws',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Governing Laws'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='limited_warranty',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Limited Warranty'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='taxes',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Taxes'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='termination',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Termination'),
        ),
        migrations.AlterField(
            model_name='contractsettings',
            name='timing_of_payment',
            field=models.TextField(blank=True, default=faker.providers.lorem.la.Provider.text, null=True, verbose_name='Timing of Payment'),
        ),
    ]
