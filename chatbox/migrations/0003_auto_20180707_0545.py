# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 05:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0002_auto_20180707_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='received',
            new_name='seen',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='send',
        ),
    ]
