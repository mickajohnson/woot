# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_address_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='user',
        ),
    ]
