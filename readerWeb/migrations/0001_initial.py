# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadCommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chipId', models.CharField(blank=True, max_length=20)),
                ('token', models.CharField(blank=True, max_length=50)),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
