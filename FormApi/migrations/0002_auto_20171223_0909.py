# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Year',
            field=models.IntegerField(choices=[('None', 'None'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')], default=1),
        ),
    ]
