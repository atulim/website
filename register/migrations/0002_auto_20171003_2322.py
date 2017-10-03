# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-03 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='branch',
            field=models.CharField(default='cs', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]