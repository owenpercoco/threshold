# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-30 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_editors'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group_edit',
            field=models.BooleanField(default=False),
        ),
    ]
