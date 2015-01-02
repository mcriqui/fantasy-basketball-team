# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0006_auto_20150102_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='away_team',
        ),
        migrations.RemoveField(
            model_name='game',
            name='home_team',
        ),
    ]
