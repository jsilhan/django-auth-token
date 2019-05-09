# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-09 12:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('auth_token', '0007_auto_20190313_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicekey',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True,
                                       verbose_name='vytvořeno dne'),
        ),
        migrations.AlterField(
            model_name='devicekey',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='aktivní?'),
        ),
        migrations.AlterField(
            model_name='devicekey',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True,
                                       verbose_name='poslední přihlášení'),
        ),
        migrations.AlterField(
            model_name='devicekey',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL, verbose_name='uživatel'),
        ),
        migrations.AlterField(
            model_name='devicekey',
            name='uuid',
            field=models.CharField(max_length=32, unique=True,
                                   verbose_name='UUID'),
        ),
    ]