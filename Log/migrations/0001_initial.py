# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0004_auto_20170313_1617'),
        ('assets', '0004_auto_20170308_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.IntegerField(choices=[(0, 'CMD'), (1, 'Login'), (2, 'Logout'), (3, 'GetFile'), (4, 'SendFile'), (5, 'exception')], default=0)),
                ('cmd', models.TextField(blank=True, null=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.DateTimeField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Server')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
            options={
                'verbose_name': '\u5ba1\u8ba1\u65e5\u5fd7',
                'verbose_name_plural': '\u5ba1\u8ba1\u65e5\u5fd7',
            },
        ),
    ]
