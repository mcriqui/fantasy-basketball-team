# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_game_team_fields(apps, schema_editor):
        Game = apps.get_model("basketball", "Game")
        Team = apps.get_model("basketball", "Team")
        for game in Game.objects.all():
            home_team = game.home_team.split(' ')
            try:
                game.home = Team.objects.get(mascot__endswith=home_team[-1])
            except:
                pass
            away_team = game.away_team.split(' ')
            try:
                game.away = Team.objects.get(mascot__endswith=away_team[-1])
            except:
                pass
            game.save()


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0005_auto_20150102_2220'),
    ]

    operations = [
        migrations.RunPython(create_game_team_fields)
    ]
