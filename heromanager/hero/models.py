from django.db import models
from hero.misc import InGameDate

# a collection of all the models of the app

class Player(models.Model):
    """
    A player represents a registered user how plays one or more charakters
    """

    name = models.CharField(max_length = 200)
    date_registered = models.DateTimeField('date registered')

    def __str__(self):
        return self.name

class Group(models.Model):
    """
    The group is a couple of charakters and players regularly playing with each
    other
    """

    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Hero(models.Model):
    """
    The hero represents a player character in a playing group. It needs to
    be owned by a player.
    """

    name = models.CharField(max_length = 200)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Diary(models.Model):
    """
    The diary of a hero stores all the things s*he has witnessed in his*her life.
    """

    owner = models.ForeignKey(Player, on_delete = models.CASCADE)
    def __str__(self):
        return self.owner.object.name + ' Tagebuch'

class DiaryEntry(models.Model):
    """
    A diary entry represents a round of gaming
    """
    
    diary = models.ForeignKey(Diary, on_delete = models.CASCADE)
    date_registered = models.DateTimeField('date registered')
    name = models.CharField(max_length = 200)
    date = models.IntegerField('in game date')

    entry = models.TextField("Eintrag")

    def getDate(self):
        timestamp = self.date.object

        return InGameDate(timestamp)
