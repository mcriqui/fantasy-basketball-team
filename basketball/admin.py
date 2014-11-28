from django.contrib import admin

from basketball.models import Game, Player
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team','played_on_time', 'played_on_date', 'tv_channel')
    list_filter = ('tv_channel', 'home_team', 'away_team')

admin.site.register(Game, GameAdmin)

admin.site.register(Player)
