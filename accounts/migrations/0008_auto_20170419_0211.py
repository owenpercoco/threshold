# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-19 02:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170412_1353'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group_Sets',
            new_name='User_Group',
        ),
    ]