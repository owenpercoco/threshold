# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20170423_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(default=b'avatars/default.jpg', upload_to=b'avatars/')),
            ],
        ),


        migrations.AddField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
