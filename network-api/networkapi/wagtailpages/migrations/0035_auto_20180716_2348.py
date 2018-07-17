# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-16 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0034_auto_20180716_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitiativeSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionHeader', models.CharField(blank=True, max_length=250)),
                ('sectionCopy', models.CharField(blank=True, max_length=250)),
                ('sectionButtonTitle', models.CharField(blank=True, max_length=250)),
                ('sectionButtonURL', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='initiativespage',
            name='sectionButtonTitle',
        ),
        migrations.RemoveField(
            model_name='initiativespage',
            name='sectionButtonURL',
        ),
        migrations.RemoveField(
            model_name='initiativespage',
            name='sectionCopy',
        ),
        migrations.RemoveField(
            model_name='initiativespage',
            name='sectionHeader',
        ),
        migrations.AddField(
            model_name='initiativesection',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiative_sections', to='wagtailpages.InitiativesPage'),
        ),
    ]
