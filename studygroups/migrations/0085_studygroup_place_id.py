# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-20 04:32


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0084_auto_20180215_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='place_id',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
