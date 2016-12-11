# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20161208_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='HeightUnits',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='WeightUnits',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]