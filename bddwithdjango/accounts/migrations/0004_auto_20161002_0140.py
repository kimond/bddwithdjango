# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 01:40
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160930_1851'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.CustomUserManagaer()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
