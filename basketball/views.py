from django.shortcuts import render
import datetime
from basketball.models import Game, Player
from django.db.models import Q


# def todays_date(request):
#     game_list = Game.objects.filter(played_on_date=datetime.date.today()).order_by('-played_on_time')
#     context = {'game_list': game_list}
#     return render(request, 'home.html', context)


def todays_date(request):
    players = Player.objects.all()
    players_teams = [team.team for team in players]
    game_list = Game.objects.filter(Q(home__in=players_teams) | Q(away__in=players_teams)).filter(played_on_date=datetime.date.today())
    context = {'game_list': game_list}
    return render(request, 'home.html', context)
