# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-07 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import profil.models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_auto_20170104_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=profil.models.upload_location),
        ),
        migrations.AlterField(
            model_name='profil',
            name='bahasa',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profil',
            name='keahlian',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]