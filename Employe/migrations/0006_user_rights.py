# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employe', '0005_auto_20160711_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_rights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=2)),
                ('type', models.IntegerField(max_length=1)),
            ],
        ),
    ]