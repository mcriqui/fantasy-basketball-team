from django.contrib import admin

from basketball.models import Game, Player, Team
# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'played_on_time', 'played_on_date', 'tv_channel')
    list_filter = ('tv_channel', 'home_team', 'away_team')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('city', 'mascot')


admin.site.register(Game, GameAdmin)

admin.site.register(Player, PlayerAdmin)

admin.site.register(Team, TeamAdmin)
