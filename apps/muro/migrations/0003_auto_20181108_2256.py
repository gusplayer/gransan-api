# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0002_auto_20181108_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_vencimiento',
            field=models.DateTimeField(),
        ),
    ]
