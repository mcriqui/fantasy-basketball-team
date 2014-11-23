from django.db import models


# Create your models here.
class Game(models.Model):
    played_on = models.DateTimeField()
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    tv_channel = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        pass


class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image_url = models.URLField()

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        pass

