# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0012_auto_20160905_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='mergemsg',
            name='uuid',
            field=models.CharField(db_index=True, default='00000000000000000000000000000000', max_length=36),
        ),
    ]