# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20)),
                ('razonS', models.CharField(max_length=80)),
                ('dirp', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
    ]
