# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 12:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20161121_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='doc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
