# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_fk',
            field=models.ForeignKey(blank=True, to='basketball.Team', null=True),
            preserve_default=True,
        ),
    ]
