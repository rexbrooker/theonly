# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theonly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='tap_number',
            field=models.IntegerField(unique=True),
        ),
    ]
