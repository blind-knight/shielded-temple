# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_case_caseid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='patient',
            new_name='patientob',
        ),
    ]
