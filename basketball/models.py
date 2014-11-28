from django.db import models


# Create your models here.
class Game(models.Model):
    played_on_date = models.DateField()
    played_on_time = models.TimeField(null=True, blank=True)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    tv_channel = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return '{0} vs {1}'.format(self.home_team, self.away_team)


class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey_number = models.IntegerField(null=True, blank=True)
    team = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    # def __str__(self):
        # 'Player'
