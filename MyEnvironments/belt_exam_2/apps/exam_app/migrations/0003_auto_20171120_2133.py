# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_auto_20171120_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
