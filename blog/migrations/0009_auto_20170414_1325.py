# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-14 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170412_1353'),
        ('blog', '0008_auto_20170414_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False),
        )
    ]