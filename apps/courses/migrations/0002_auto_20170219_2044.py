# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]