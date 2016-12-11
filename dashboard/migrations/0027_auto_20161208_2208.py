# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_auto_20161208_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='HeightUnits',
            field=models.CharField(default='cm', max_length=10),
        ),
        migrations.AddField(
            model_name='case',
            name='WeightUnits',
            field=models.CharField(default='kg', max_length=10),
        ),
    ]