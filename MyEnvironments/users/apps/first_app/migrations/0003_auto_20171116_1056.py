# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20171115_2101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='Profile',
        ),
    ]
