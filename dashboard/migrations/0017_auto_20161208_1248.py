# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_case_patientob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='Height',
            field=models.CharField(max_length=10),
        ),
    ]
