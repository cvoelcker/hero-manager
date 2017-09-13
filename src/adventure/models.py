from django.db import models
from django.utils import timezone
from hero.models import Group, Hero


class Adventure(models.Model):
    """

    """

    class Meta:
        unique_together = ('group', 'name')

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ongoing = models.BooleanField(default=False)

    name = models.CharField(max_length=200)

    date_started = models.DateField(default=timezone.now)

    description = models.TextField()

    def __str__(self):
        return self.name


class DiaryEntry(models.Model):
    """
    An entry into a diary
    """

    class Meta:
        ordering = ('adventure', 'date')

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.SET_NULL,
                                  null=True)
    date_registered = models.DateTimeField(
        'date added',
        default=timezone.now)
    name = models.CharField(max_length=200)
    date = models.IntegerField('in game date')

    entry = models.TextField('entry')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "{}: {} {}".format(
                str(self.adventure),
                str(self.hero),
                self.date
            )


class NSCGroup(models.Model):
    """
    Models a group of NSCs united by concurrent
    """

    class Meta:
        unique_together = ('adventure', 'name')

    adventure = models.ForeignKey(Adventure)

    name = models.TextField()
    description = models.TextField()

    color = models.CharField(max_length=7)


class NSC(models.Model):
    """

    """

    name = models.TextField()
    description = models.TextField()

    groups = models.ManyToManyField(NSCGroup)
