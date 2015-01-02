# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0004_auto_20150102_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away',
            field=models.ForeignKey(related_name=b'away_games', blank=True, to='basketball.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home',
            field=models.ForeignKey(related_name=b'home_games', blank=True, to='basketball.Team', null=True),
            preserve_default=True,
        ),
    ]
