# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-12 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170411_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_sets',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
