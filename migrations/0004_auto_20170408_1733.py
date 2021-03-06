# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theonly', '0003_auto_20170408_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menumodel',
            options={'ordering': ['menu_row', 'tap_number']},
        ),
        migrations.AddField(
            model_name='beverage',
            name='beverage_color',
            field=models.CharField(default='ffff00', max_length=6, verbose_name='Hash of beverage color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menumodel',
            name='tap_number_subtext',
            field=models.CharField(default='', max_length=6, verbose_name='text under tap number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beverage',
            name='beverage_name',
            field=models.CharField(max_length=2048, verbose_name='beverage name'),
        ),
    ]
