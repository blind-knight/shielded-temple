# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_auto_20161208_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='HeightUnits',
            field=models.CharField(default='cm', max_length=20, verbose_name='HeightUnits:'),
        ),
    ]
