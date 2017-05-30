# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-09 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=7)),
                ('secondary_color', models.CharField(max_length=7)),
                ('third_color', models.CharField(max_length=7)),
            ],
        ),
    ]
