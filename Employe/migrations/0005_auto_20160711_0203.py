# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employe', '0004_recruiter_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]