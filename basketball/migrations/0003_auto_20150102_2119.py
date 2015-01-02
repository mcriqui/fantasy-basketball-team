# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def make_team_fk_field(apps, schema_editor):
        Player = apps.get_model("basketball", "Player")
        Team = apps.get_model("basketball", "Team")
        for player in Player.objects.all():
            team = player.team.split(' ')
            player.team_fk = Team.objects.get(mascot__endswith=team[-1])
            player.save()


class Migration(migrations.Migration):


    dependencies = [
        ('basketball', '0002_player_team_fk'),
    ]

    operations = [
        migrations.RunPython(make_team_fk_field)
    ]
