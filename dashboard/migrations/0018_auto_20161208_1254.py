# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20161208_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='Height',
            field=models.CharField(max_length=20),
        ),
    ]
