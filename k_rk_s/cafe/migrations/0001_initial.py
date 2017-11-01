# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('main_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='CafeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_images', to='cafe.Cafe')),
            ],
        ),
    ]
