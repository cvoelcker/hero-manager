from django.db import models
from django.utils import timezone
from hero.models import Group, Hero


class Adventure(models.Model):
    """

    """

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ongoing = models.BooleanField(default=False)

    name = models.CharField(max_length=200)

    date_started = models.DateField(default=timezone.now)

    description = models.TextField()


class DiaryEntry(models.Model):
    """
    An entry into a diary
    """

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.SET_NULL,
                                  null=True)
    date_registered = models.DateTimeField(
        'date added',
        default=timezone.now)
    name = models.CharField(max_length=200)
    date = models.IntegerField('in game date')

    entry = models.TextField('entry')
