# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0003_auto_20150102_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='team_fk',
            new_name='team'
        ),
    ]
