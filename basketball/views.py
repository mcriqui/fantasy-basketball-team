from django.shortcuts import render
import datetime
from basketball.models import Game


def todays_date(request):
    game_list = Game.objects.filter(played_on_date=datetime.date.today()).order_by('-played_on_time')
    context = {'game_list': game_list}
    return render(request, 'home.html', context)
