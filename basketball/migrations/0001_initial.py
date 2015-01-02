# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('played_on_date', models.DateField()),
                ('played_on_time', models.TimeField(null=True, blank=True)),
                ('home_team', models.CharField(max_length=50)),
                ('away_team', models.CharField(max_length=50)),
                ('tv_channel', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('jersey_number', models.IntegerField(null=True, blank=True)),
                ('team', models.CharField(max_length=50, null=True, blank=True)),
                ('position', models.CharField(max_length=50, null=True, blank=True)),
                ('image_url', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('mascot', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
    ]
