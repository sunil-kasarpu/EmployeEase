# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employe', '0003_auto_20160703_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='contact',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
