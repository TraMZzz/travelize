# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diller', '0002_diller_airport'),
    ]

    operations = [
        migrations.AddField(
            model_name='diller',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=20),
        ),
    ]
