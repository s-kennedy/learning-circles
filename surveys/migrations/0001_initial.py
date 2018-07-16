# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-16 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studygroups', '0093_application_mobile_opt_out_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilitatorSurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeform_key', models.CharField(max_length=64, unique=True)),
                ('survey', models.TextField()),
                ('response', models.TextField()),
                ('responded_at', models.DateTimeField()),
                ('study_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studygroups.StudyGroup')),
            ],
        ),
    ]
