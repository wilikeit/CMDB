# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20170317_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='cabinet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.Cabinet', verbose_name='\u673a\u67dc'),
            preserve_default=False,
        ),
    ]
