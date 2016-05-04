# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gethistoryfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('date_searched', models.DateTimeField()),
                ('last_visited', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]