# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20160407_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='page_json',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
