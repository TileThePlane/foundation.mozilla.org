# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0033_auto_20180720_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiativesection',
            name='sectionButtonURL',
            field=models.TextField(verbose_name='Button URL'),
        ),
    ]