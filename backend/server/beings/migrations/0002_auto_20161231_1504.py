# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='being',
            name='routine',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='being',
            name='birth',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]