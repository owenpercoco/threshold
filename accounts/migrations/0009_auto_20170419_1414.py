# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-19 14:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170419_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_group',
            name='users',
            field=models.ManyToManyField(related_name='user_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
