from django.shortcuts import render
import datetime
from basketball.models import Game, Player
from django.db.models import Q


def todays_date(request):
    players = Player.objects.all()
    players_teams = [team.team for team in players]
    game_list = Game.objects.filter(Q(home__in=players_teams) | Q(away__in=players_teams)).filter(played_on_date=datetime.date.today())
    wizards_home = Game.objects.filter(home__city="Washington").filter(away__in=players_teams).filter(played_on_date=datetime.date.today())
    wizards_away = Game.objects.filter(away__city="Washington").filter(home__in=players_teams).filter(played_on_date=datetime.date.today())
    context = {'game_list': game_list, 'wizards_home': wizards_home, 'wizards_away': wizards_away}
    return render(request, 'home.html', context)
