# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_auto_20161208_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='patientob',
        ),
        migrations.DeleteModel(
            name='case',
        ),
    ]