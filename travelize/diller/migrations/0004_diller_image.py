# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diller', '0003_diller_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='diller',
            name='image',
            field=models.ImageField(blank=True, upload_to='event_image'),
        ),
    ]
