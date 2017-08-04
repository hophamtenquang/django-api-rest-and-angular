# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170802_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('gender', models.BinaryField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
