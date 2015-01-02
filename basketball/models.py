from django.db import models



class Game(models.Model):
    played_on_date = models.DateField()
    played_on_time = models.TimeField(null=True, blank=True)
    home = models.ForeignKey('Team', null=True, blank=True, related_name="home_games")
    away = models.ForeignKey('Team', null=True, blank=True, related_name="away_games")
    tv_channel = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return '{0} vs {1}'.format(self.home, self.away)


class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey_number = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey('Team', null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return self.name


class Team(models.Model):
    city = models.CharField(max_length=50)
    mascot = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return '{0} {1}'.format(self.city, self.mascot)
