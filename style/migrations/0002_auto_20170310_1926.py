# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-10 19:26
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=10),
        ),
    ]
