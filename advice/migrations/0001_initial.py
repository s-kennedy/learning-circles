# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-12 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('topic', models.CharField(max_length=256)),
                ('tip', models.CharField(max_length=1024)),
            ],
        ),
    ]