from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from hero import settings


class Group(models.Model):
    """
    The group is a couple of charakters and players regularly playing with each
    other
    """

    name = models.CharField(
        max_length=200,
        primary_key=True)

    rule_version = models.CharField(
        max_length=20,
        choices=settings.RULES_SUPPORTED,
        default='DEFAULT',
    )

    game_master = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='gaming_group_master'
    )

    players = models.ManyToManyField(
        User,
        related_name='gaming_group'
    )

    description = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Hero(models.Model):
    """
    The hero represents a player character in a playing group. It needs to
    be owned by a player.
    """

    name = models.CharField(max_length=200)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    char_sheet = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Diary(models.Model):
    """
    The diary of a hero stores all the things s*he has witnessed in his*her life.
    """

    owner = models.ForeignKey(Hero, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.object.name + ' Tagebuch'


class DiaryEntry(models.Model):
    """
    An entry into a diary
    """

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(
        'date added',
        default=timezone.now)
    name = models.CharField(max_length=200)
    date = models.IntegerField('in game date')

    entry = models.TextField("Eintrag")
