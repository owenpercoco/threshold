# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-12 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170412_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]