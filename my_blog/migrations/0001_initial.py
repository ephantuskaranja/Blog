# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 16:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(blank=True)),
                ('created_at', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
