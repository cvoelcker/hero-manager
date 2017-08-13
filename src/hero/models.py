from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . import xml_hero


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
        choices=xml_hero.RULES_SUPPORTED,
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

    def has_charsheets(self):
        return xml_hero.has_charsheet(self.rule_version)


class Hero(models.Model):
    """
    The hero represents a player character in a playing group. It needs to
    be owned by a player.
    """

    class Meta:
        unique_together = ('group', 'name')

    name = models.CharField(max_length=200)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    char_sheet = models.FileField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_char_sheet(self):
        return xml_hero.get_hero(self.group.rule_version, self.char_sheet)
