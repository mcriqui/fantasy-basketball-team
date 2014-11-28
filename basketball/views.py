from django.shortcuts import render, render_to_response
import datetime
from basketball.models import Game
from django.http import HttpResponse



def todays_date(request):
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    todays_date = "{0}-{1}".format(month, day)
    game_list = Game.objects.filter(played_on_date__contains=todays_date).order_by('-played_on_time')
    context = {'game_list': game_list}
    return render(request, 'home.html', context)

